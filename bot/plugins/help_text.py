import pyrogram 
from pyrogram.types import filters, InlineKeyboardButton, InlineKeyboardMarkup 
from bot.localisation import Localisation
from pyrogram.errors import UserNotParticipant, UserBannedInChannel

from pyrogram.handlers import (
   Client,
   filters,
   CallbackQueryHandler, 
   MessageHandler
)
 
@Client.on_message()
async def pm(bot, update):
 try:
    chat = await bot.get_chat_member(-1001221642755, update.from_user.id)
    if chat.status=='kicked':
        return await update.reply_text('😡 Hai you are kicked from my updates channel. So, you are not able to use me 😝')
 except UserBannedInChannel:
     return await update.reply_text("Hai you made a mistake so you are banned from channel so you are banned from me too 😜")
 except UserNotParticipant:
   button = [[InlineKeyboardButton('join Updates channel 🥰', url='https://t.me/Ns_bot_updates')], [InlineKeyboardButton('Refresh 🔄', callback_data='refresh')]]
   markup = InlineKeyboardMarkup(button)
   return await update.reply_text(text="""Hai bro,\n\n**You must join my channel for using my bot.**\n\nPress this button to join now 👇""", parse_mode='markdown', reply_to_message_id=update.message_id, reply_markup=markup)
 update.continue_propagation()



@Client.on_message(filters.command(["start"]))
async def start(bot, update):
      await update.reply_text(text=Localisation.START_TEXT.format(update.from_user.first_name),
                              parse_mode="markdown",
                              disable_web_page_preview=True,
                              reply_to_message_id=update.message_id,
                              reply_markup=InlineKeyboardMarkup(
                              [
                               [
                               InlineKeyboardButton("My Father", url="https://t.me/Ns_AnoNymous"),
                               InlineKeyboardButton("About 🤖", callback_data='about')
                               ],
                               [
                               InlineKeyboardButton("How to use me ?🤔", callback_data='help'),
                               InlineKeyboardButton("Close 🔐", callback_data='close')
                               ]
                              ]
                            )
                          )

@Client.on_message(filters.command(["help"]))
async def help(bot, update):
      await update.reply_text(text=Localisation.HELP_TEXT.format(update.from_user.first_name),
                              parse_mode="markdown",
                              reply_to_message_id=update.message_id,
                              reply_markup=InlineKeyboardMarkup(
                              [
                               [
                               InlineKeyboardButton("Home 🏠", callback_data='home'),
                               InlineKeyboardButton("Close 🔐", callback_data='close')
                               ]
                              ]
                            )
                          )


@Client.on_message(filters.command(["about"]))
async def about(bot, update):
      await update.reply_text(text=Localisation.ABOUT_TEXT.format(update.from_user.first_name),
                              parse_mode="markdown",
                              reply_to_message_id=update.message_id,
                              reply_markup=InlineKeyboardMarkup(
                              [
                               [
                               InlineKeyboardButton("Home 🏠", callback_data='home'),
                               InlineKeyboardButton("Close 🔐", callback_data='close')
                               ]
                              ]
                            )
                          )



