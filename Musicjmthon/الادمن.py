from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, call_py
from Musicjmthon.helpers.decorators import authorized_users_only
from Musicjmthon.helpers.handlers import skip_current_song, skip_item
from Musicjmthon.helpers.queues import QUEUE, clear_queue


@Client.on_message(filters.command(["تخطي"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**مفيش حاجة مطلوبه اتخطي اي يسطا ؟؟**")
        elif op == 1:
            await m.reply("**")
        else:
            await m.reply(
                f"**⏭ تخطي التشغيل** \n**🎧 المشغل الحالي ** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**مسحت الاغنيه من قائمة الانتظار يعم .**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(filters.command(["ايقاف", "end"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**قفلت الاغنيه بطل لعب بقا x**")
        except Exception as e:
            await m.reply(f"**ف خطأ يسطا اتفضل صلحو .** \n`{e}`")
    else:
        await m.reply("**مفيش حاجة شغاله اقفل اي !**")


@Client.on_message(filters.command(["وقف"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**⏸ وقفتلك الاغنيه مؤقت يعم اهو.**\n\n•لتكملة الاغنيه ، اكتب  » {HNDLR}كمل"
            )
        except Exception as e:
            await m.reply(f"**ف خطأ يسطا اتفضل صلحو .** \n`{e}`")
    else:
        await m.reply("**مفيش حاجة اشتغلت اصلا !**")


@Client.on_message(filters.command(["كمل"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶ كملتلك الاغنيه يعم اهو من التوقيف المؤقت**\n\n •  لتوقيف الاغنيه مؤقت ، اكتب » {HNDLR}وقف**"
            )
        except Exception as e:
            await m.reply(f"**خطأ** \n`{e}`")
    else:
        await m.reply("**مفيش حاجة وقفت مؤقت اصلا !**")
