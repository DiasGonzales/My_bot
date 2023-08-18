from aiogram import types
from database.manager import CategoryManager, FilmManager
from bot_utils.keyboards import get_category_btns

async def welcome_message(message:types.Message):
    text = """
        Приветствую тебя смертный, я бот для игры в угадай фильм по эмоджи.\nЧтобы начать игру, отправь мне сообщение "Start"
    """
    
    await message.answer(text)
    
async def start_game(message:types.Message):
    text = "Выберите категорию игры"
    markup = get_category_btns()
    await message.answer(text, reply_markup=markup)
    
    
async def get_movie(message:types.Message):
    films = FilmManager().get_films()
    for f in films:
        await message.answer(f"{f.emoji_text}")
        
        
        
