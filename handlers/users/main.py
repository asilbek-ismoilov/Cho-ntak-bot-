from aiogram.types import Message, CallbackQuery
from loader import dp, db, bot, ADMINS
from aiogram import F
from states.help_stt import Eslatma
from aiogram.fsm.context import FSMContext
from keyboard_buttons.inline.menu import menu


@dp.message(F.text =="Qo'shish +")
async def qoshish(message:Message,state:FSMContext):
    await message.answer("Eslatuvchi xabar nomini kiriting")
    
    await state.set_state(Eslatma.nomi)

@dp.message(Eslatma.nomi)
async def name(message:Message,state:FSMContext):
    name =  message.text
    await state.update_data(name = name)
    await message.answer(f"Endi {name} uchun. Menga istalgan ma'lumotni kiriting")
    await state.set_state(Eslatma.eslatma)

@dp.message(Eslatma.eslatma)
async def eslatma(message:Message,state:FSMContext):
    from_chat_id = message.from_user.id

    await state.update_data(eslatma = message.message_id)
    data = await state.get_data()
    name = data.get("name")

    await bot.copy_message(chat_id=ADMINS[0], from_chat_id=from_chat_id, message_id=message.message_id, caption=name, reply_markup=menu)
    await state.clear()

@dp.callback_query(F.data=="true")
async def tastiqlash(callback:CallbackQuery, state: FSMContext):
    telegram_id = callback.message.from_user.id
    data = await state.get_data()
    name = data.get("name")
    eslatma = data.get("eslatma")

    db.add_user(telegram_id=telegram_id, name=name, text_id=eslatma)

    await callback.message.answer("Malumot muvaffaqiyatli qo'shildi !")
    


@dp.callback_query(F.data=="false")
async def bekor_qilish(callback:CallbackQuery, state: FSMContext):
    await callback.message.answer("Qayta boshlash")
    await state.clear()
    await state.set_state(Eslatma.nomi)
    await callback.message.answer("Eslatuvchi xabar nomini kiriting")
    
