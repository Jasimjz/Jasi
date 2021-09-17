from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("📢Support Group", url="HTTPS://t.me/jzmodsofc")],
		[InlineKeyboardButton("Channel", url="https://t.me/jzmodsyt")]
                ])

	help_image = "https://telegra.ph/file/de0aebb87a93cdff61c0c.jpg"
	await message.reply_photo(help_image,  caption="HELP 📃...**\n \n__• Just Youtube video url 🌟__ \n__• Select video/mp3 format __\n  \n__• ```Bot Deployed By Jasim & Arsal``` 🚨\n",reply_markup=alpha2)
