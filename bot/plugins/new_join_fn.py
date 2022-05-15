#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K


from bot.localisation import Localisation



async def help_message_f(client, message):
    # display the /help message
    await message.reply_text(
        Localisation.HELP_MESSAGE,
        quote=True
    )
