from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Namuna inline
menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tastiqlash✅", callback_data="true"), 
            InlineKeyboardButton(text="Taxrirlash✏️", callback_data="false"), 
        ]
    ]
)
