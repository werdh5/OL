import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("الأحد", 60 * 60 * 24 * 7),
    ("يوم", 60 * 60 * 24),
    ("الساعة", 60 * 60),
    ("الدقيقة", 60),
    ("الثانيه", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنك"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🏓 بـنـك/b> `{delta_ping * 1000:.3f} بالثانيه` \n<b>⏳ شغال</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["اعادة تشغيل"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    fire = await m.reply("1")
    await fire.edit("2")
    await fire.edit("3")
    await fire.edit("4")
    await fire.edit("5")
    await fire.edit("6")
    await fire.edit("7")
    await fire.edit("8")
    await fire.edit("9")
    await fire.edit("**تم اعادة تشغيل السورس بنجاح ✓**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["الاوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HEPZ = f"""
- مـرحبا {m.from_user.mention}!

• هذه هي قائمـة اوامر السـورس .
•═════•| sezr |•═════•

• قناة السورس : @so_alfaa
• قناة السورس : @me_xec_o
• جروب الدعم : @LURA205
•═════•| 𝙻𝚞𝚛𝚊 |•═════•


• اوامر المستخدمين

• {HNDLR}لتشغيل اغنيه ف الكول اكتب [ تشغيل او play ]

• {HNDLR}لتشغيل فديو ف الكول اكتب  [ فيديو ]
• {HNDLR}لعرض قائمة التشغيل اكتب [ القائمة ]

• {HNDLR}لعرض سرعه النت للبوت اكتب [ بنك ]
• {HNDLR}لعرض اوامر سورس لورا ميوزك اكتب [ الاوامر ]

• اوامر المشرفين .
 
• {HNDLR}لتكملة تشغيل الاغنيه اكتب [ كمل ]

• {HNDLR}عشان توقف الاغنيه مؤقت اكتب [ وقف ]

• {HNDLR}لتخطي الاغنيه او الفديو اكتب [ تخطي ]

• {HNDLR}لايقاف تشغيل الاغاني اكتب  [ ايقاف ]
"""
    await m.reply(HEPZ)


@Client.on_message(filters.command(["السورس"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPZ = f"""
<b>- اهلا {m.from_user.mention} !
•═════•| 𝙻𝚞𝚛𝚊 |•═════•

• سورس لورا و مكس ميوزك .
• اختصاص البوت تشغيل الاغاني او الفديوهات ف الكول .
• لعرض اوامر السورس اكتب  {HNDLR}الاوامر .
•═════•| 𝙻𝚞𝚛𝚊 |•═════•
• قناة سورس لورا  : @so_alfaa
• قناة سورس مكس  : @me_xec_o
• جروب الدعم : @LURA205
"""
    await m.reply(REPZ, disable_web_page_preview=True)
