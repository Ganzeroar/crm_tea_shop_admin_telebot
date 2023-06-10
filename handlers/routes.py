from loader import dp


def create_routes():
    from handlers import handlers
    dp.register_message_handler(
        handlers.start_return_user_id,
        commands=['start'],
    )

    dp.register_message_handler(
        handlers.return_user_id,
        content_types=['text'],
    )
