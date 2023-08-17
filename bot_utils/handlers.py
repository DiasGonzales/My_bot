from aiogram import types



async def welcome_message(message:types.Message):
    text = """
        Приветствую тебя смертный, я бот для игры в угадай фильм по эмоджи.\nЧтобы начать игру, отправь мне сообщение "Start"
    """
    
    await message.answer(text)
    
    
    