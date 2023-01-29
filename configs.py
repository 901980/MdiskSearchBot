# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 11508650))
    API_HASH = os.environ.get("API_HASH", "d4053a01b1c02f705c45a1e30496d11e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6199157936:AAG6cemg4C_bW4sDNEe8nCU5jxTUQX91x6I")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001628019485))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "SM_link_search_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1661411006))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/SM_Updates_1'Link Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/White_devil_123'>Cynite</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/cyniteofficial'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @White_devil_123</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @White_devil_123</a></b>
"""


