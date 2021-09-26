from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Просто Отправьте Url-Адрес Youtube"
    await message.reply_text(helptxt)
