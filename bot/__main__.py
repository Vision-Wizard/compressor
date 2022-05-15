#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K


import os

from bot import (
    APP_ID,
    API_HASH,
    AUTH_USERS,
    DOWNLOAD_LOCATION,
    LOGGER,
    TG_BOT_TOKEN
)
from bot.plugins.new_join_fn import (	
    help_message_f	
)

from pyrogram import (
  Client, 
  Filters, 
  MessageHandler,
  CallbackQueryHandler
)

from bot.plugins.incoming_message_fn import (
    incoming_compress_message_f,
    incoming_cancel_message_f
)


from bot.plugins.status_message_fn import (
    exec_message_f,
    upload_log_file
)

from bot.commands import Command
from bot.plugins.call_back_button_handler import button

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    #
    sessions = "/app/sessions"
    if not os.path.isdir(sessions):
        os.makedirs(sessions)
    app = Client(
        "Compress",
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=2,
        plugins = dict(
             root="bot/plugins"
      )
    )
    #
    app.set_parse_mode("html")
    #

    # COMPRESS command
    incoming_compress_message_handler = MessageHandler(
        incoming_compress_message_f,
        filters=Filters.command([Command.COMPRESS])
    )
    app.add_handler(incoming_compress_message_handler)
    
    # CANCEL command
    incoming_cancel_message_handler = MessageHandler(
        incoming_cancel_message_f,
        filters=Filters.command([Command.CANCEL])
    )
    app.add_handler(incoming_cancel_message_handler)

    # MEMEs COMMANDs
    exec_message_handler = MessageHandler(
        exec_message_f,
        filters=Filters.command([Command.EXEC])
    )
    app.add_handler(exec_message_handler)
    
    
    # Telegram command to upload LOG files
    upload_log_f_handler = MessageHandler(
        upload_log_file,
        filters=Filters.command([Command.UPLOAD_LOG_FILE]) & Filters.chat(chats=AUTH_USERS)       
    )
    app.add_handler(upload_log_f_handler)
    
    call_back_button_handler = CallbackQueryHandler(
        button
    )
    app.add_handler(call_back_button_handler)

    # run the APPlication
    app.run()
