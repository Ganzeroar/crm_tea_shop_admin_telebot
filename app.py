#! /usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import logging
from aiohttp import web

from aiogram import types

from loader import dp, bot


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Start bot'),
    ])


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)


logging.basicConfig(
    level=logging.INFO,
    filename='telebot.log',
    filemode='a',
    format='TIME - %(asctime)s\nLEVEL - %(levelname)s\nNAME -- %(name)s\nMESSAGE - %(message)s\n',
)


async def start_polling():
    await set_default_commands(dp)
    await dp.start_polling()


routes = web.RouteTableDef()


@routes.post('/new_order')
async def handle_new_order_notification(request):
    print(request)
    data = await request.json()
    telegram_user_id = data['telegram_user_id']
    notification_message = data['notification_message']
    await send_notification_about_new_order(telegram_user_id, notification_message)
    print(dir(request))
    return web.Response(text="OK")


async def send_notification_about_new_order(user_id, notification_message):
    await bot.send_message(user_id, notification_message)


app = web.Application()
app.add_routes(routes)


async def run_aiohttp_server():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8888)
    await site.start()


async def create_task_group():
    await asyncio.gather(
        start_polling(),
        run_aiohttp_server(),
    )

if __name__ == '__main__':
    asyncio.new_event_loop().run_until_complete(create_task_group())
