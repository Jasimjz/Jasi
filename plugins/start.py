from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Alpha = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("📌️ Support Group🔎", url="https://t.me/jzmodsofc")],
        [InlineKeyboardButton("📌️ Tg Channel 🔎", url="https://t.me/jzmodsyt")]

    ])
    thumbnail_url = "https://telegra.ph/file/de0aebb87a93cdff61c0c.jpg"
    await message.reply_photo(thumbnail_url, caption=f"**🙂 Hi <b>{message.from_user.first_name}**</b>\n\n<br>__😇 I Can Download YT Videos For You ✨️__</br>\n\n<b>• **🗂️ Instructions for use...🚨**</b>\n• **⚙ Type /help to get instructins...**\n \n───── ❝ **Lets Start** ❞ ─────\n ", reply_markup=Alpha)
    raise StopPropagation
