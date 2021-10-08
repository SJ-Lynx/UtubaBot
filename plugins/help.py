from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"🔎 для поиска воспользуйтесь @vid или @youtube. Введите в чате @vid и запрос. \n\n🔗 отправьте ссылку YouTube, чтобы скачать видео или аудио. "
    await message.reply_text(helptxt)
