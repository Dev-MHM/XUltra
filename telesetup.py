#!/usr/bin/env python3
# (c) https://t.me/MHMOFFICIAL
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details""")
APP_ID = 1051375
API_HASH = 'df4f7a6255a1d93b972f952d9d285c1e'

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
