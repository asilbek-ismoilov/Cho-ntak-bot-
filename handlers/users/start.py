from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.default.bt import add

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    user = db.select_user(telegram_id=telegram_id)
    if not user:
        db.add_user(full_name=full_name, telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz")
    else:
        await message.answer(text="Assalomu alaykum", reply_markup=add)
