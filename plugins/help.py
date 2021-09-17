from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("SUPPORT GROUP", url="https://t.me/jzmodsofc")],
		[InlineKeyboardButton("CHANNEL", url="https://t.me/jzmodsyt")]
                ])

	help_image = "https://telegra.ph/file/8e3d7e8da2d02d3bd4b75.jpg"
	await message.reply_photo(help_image,  caption="**HELP 📃...**\n \n__•Send your Youtube video url 🌟__ \n__• And select The format click /help for more info \n",reply_markup=alpha2)
