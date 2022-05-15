#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52

# the logging things

from bot.helper_funcs.utils import(
    delete_downloads
)
from bot.localisation import Localisation
import logging
import os
import json
import shutil
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)
from pyrogram.errors import UserNotParticipant, UserBannedInChannel 
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup 
#from bot.helper_funcs.admin_check import AdminCheck
from bot import (
    AUTH_USERS,
    DOWNLOAD_LOCATION
)
from .incoming_message_fn import Active_user


async def force(bot, update: CallbackQuery):
 try:
    chat = await bot.get_chat_member(-1001221642755, update.from_user.id)
    if chat.status=='kicked':
        return await update.message.edit('😡 Hai you are kicked from my updates channel. So, you are not able to use me 😝')
 except UserBannedInChannel:
     return await update.message.edit("Hai you made a mistake so you are banned from channel so you are banned from me too 😜")
 except UserNotParticipant:
   button = [[InlineKeyboardButton('join Updates channel 🥰', url='https://t.me/Ns_bot_updates')], [InlineKeyboardButton('Refresh 🔄', callback_data='refresh')]]
   markup = InlineKeyboardMarkup(button)
   return await update.message.edit(text="""Hai bro,\n\n**You must join my channel for using my bot.**\n\nPress this button to join now 👇""", parse_mode='markdown', reply_to_message_id=update.message_id, reply_markup=markup)
 update.continue_propagation()

async def button(bot, update: CallbackQuery):
    cb_data = update.data
    try:
        g = await AdminCheck(bot, update.message.chat.id, update.from_user.id)
        print(g)
    except:
        pass
    LOGGER.info(update.message.reply_to_message.from_user.id)
    if (update.from_user.id == update.message.reply_to_message.from_user.id) or g:
        print(cb_data)
        if cb_data == "fuckingdo":
            if (update.from_user.id in AUTH_USERS)|(update.from_user.id in Active_user):
                status = DOWNLOAD_LOCATION + "/status.json"
                with open(status, 'r+') as f:
                    statusMsg = json.load(f)
                    statusMsg['running'] = False
                    f.seek(0)
                    json.dump(statusMsg, f, indent=2)
                    if 'pid' in statusMsg.keys():
                        try:
                            os.kill(statusMsg["pid"], 9)
                        except:
                            pass
                        delete_downloads()
                    try:
                        await bot.delete_messages(update.message.chat.id, statusMsg["message"])
                    except:
                        pass
                    try:
                        Active_user.remove(Active_user[0])
                        await update.message.edit_text("🚦🚦 Stopped 🚦🚦")
                    except:
                        pass
            else:
                try:
                    await update.message.edit_text("You are not allowed to do that 🤭")
                except:
                    pass
        if cb_data == "fuckoff":
            try:
                await update.message.edit_text("Okay! fine 🤬")
            except:
                pass
		

        if 'help' in update.data:
            await update.message.edit(text=Localisation.HELP_TEXT.format(update.message.reply_to_message.from_user.first_name),
                 parse_mode="markdown",
                 disable_web_page_preview=True,
                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Home 🏠', callback_data='back'), InlineKeyboardButton('Close 🔐', callback_data='close')]])
                  )

        if 'close' in update.data:
          await update.message.delete()
          await update.message.reply_to_message.delete()

        if 'back' in update.data:
          await update.message.edit(text=Localisation.START_TEXT.format(update.message.reply_to_message.from_user.first_name), 
                parse_mode='markdown', disable_web_page_preview=True,
                #reply_to_message='update.message_id', 
                reply_markup=InlineKeyboardMarkup(
                  [
                      [
                      InlineKeyboardButton('𝙼𝚢 𝚏𝚊𝚝𝚑𝚎𝚛 👨‍💻', url='https://t.me/Ns_AnoNymous'),
                      InlineKeyboardButton('𝙰𝚋𝚘𝚞𝚝 🤖', callback_data='about')
                      ],
                      [
                      InlineKeyboardButton('𝙷𝚘𝚠 𝚝𝚘 𝚞𝚜𝚎 𝚖𝚎  ? 🤔', callback_data="help"),
                      InlineKeyboardButton('𝙲𝚕𝚘𝚜𝚎 🔐', callback_data="close")
                      ]
                    ]
                  )
                )
        if 'about' in update.data:
          await update.message.edit(text=Localisation.ABOUT_TEXT, 
                parse_mode='markdown', disable_web_page_preview=True,
                #reply_to_message='update.message_id', 
                reply_markup=InlineKeyboardMarkup(
                 [
                  [
                  InlineKeyboardButton("Home 🏠", callback_data='back'),
                  InlineKeyboardButton('Close 🔐', callback_data='close')
                  ]
                 ]
                )
              )
        if 'refresh' in update.data:
         await update.message.edit(
           text=Localisation.START_TEXT.format(update.message.reply_to_message.from_user.first_name), 
           disable_web_page_preview=True,
           reply_markup=InlineKeyboardMarkup(
           [
             [
             InlineKeyboardButton('𝙼𝚢 𝚏𝚊𝚝𝚑𝚎𝚛 👨‍💻', url='https://t.me/Ns_AnoNymous'),
             InlineKeyboardButton('𝙰𝚋𝚘𝚞𝚝 🤖', callback_data='about')
             ],
             [
             InlineKeyboardButton('𝙷𝚘𝚠 𝚝𝚘 𝚞𝚜𝚎 𝚖𝚎  ? 🤔', callback_data="help"),
             InlineKeyboardButton('𝙲𝚕𝚘𝚜𝚎 🔐', callback_data="close")
             ]
           ]
         )
       )		
