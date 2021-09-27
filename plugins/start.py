from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Канал", url="https://t.me/SJa_bots")],
        [InlineKeyboardButton(
            "Сообщать об ошибках 😊", url="https://t.me/SJ_Lynx")]
    ])
    welcomed = f"Привет <b>{message.from_user.first_name}</b>\n/help для получения дополнительной информации"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
