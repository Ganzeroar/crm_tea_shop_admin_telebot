from aiogram.types import Message


async def start_return_user_id(message: Message):
    user_id = message.from_user.id
    answer_text = f'Здравствуйте! Ваш telegram_id: {user_id}. Используйте его для настройки прав доступа в соответствующем разделе.'
    await message.answer(answer_text)


async def return_user_id(message: Message):
    user_id = message.from_user.id
    answer_text = f'Ваш telegram_id: {user_id}. Используйте его для настройки прав доступа в соответствующем разделе.'
    await message.answer(answer_text)
