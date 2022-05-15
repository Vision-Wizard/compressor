#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hello __**{}**__, \n\nI am a Telegram Video Compress Bot. I can reduce the size of the large media but takes more time.\n\n**Maintained By:** [Anonymous 🧘‍♂️](https://t.me/Ns_AnoNymous)"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "Trying to Download to my server.....📥 \n"
    
    UPLOAD_START = "Started to Upload... 📤 \n"
    
    COMPRESS_START = "Trying to compress..."
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "<b>@compress_nsbot</b>"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already One Process going on. \n or \n A media already exists. \n  Please send /cancel to delete existing media. ⚠️"
    
    HELP_TEXT = "Hi am Video Compressor Bot \n\n1. Sent your telegram big video file \n2. Reply the file - /compress And Persentage \nEg:- `/compress 50` \n\n**Support Group :** @Ns_Bot_supporters\n**Support Channel :**@Ns_bot_updates"
    
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )
    ABOUT_TEXT = """**MY DETAILS:**

🤖My Name: [Compresser](https://t.me/compress_nsbot)
    
📝 Language: [Python 3](https://www.python.org/)

🧰 Framework: [Pyrogram](https://github.com/pyrogram/pyrogram)

👨‍💻 Developer: [𝐀𝐧𝐨𝐧𝐲𝐦𝐨𝐮𝐬](https://t.me/Ns_AnoNymouS)

📢 Channel: [NS BOT UPDATES](https://t.me/Ns_bot_updates)

👥 Group: [Ns BOT SUPPORT](https://t.me/Ns_Bot_supporters)"""

    
