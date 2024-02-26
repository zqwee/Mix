import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["","‹ اوامر التشغيل ›"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/41a777f089288f7ad2571.jpg",
        caption=f"""**- اوامر التشغيل اتبع مايلي
        
 [— — — — — — — — — —](https://graph.org/file/7f1402824c0c70c91fd81.jpg)
◇︰ تشغيل أو شغل : لبدء تشغيل الاغاني .

◇︰ بينج : لقياس سرعة النت في البوت .

◇︰أوامر القناة : تشغيل + أسم الأغنية  .

◇︰ كتم او مؤقت : لكتم الأغنية الحالية .

◇︰ كمل : لألغاء كتم الاغنية الحالية .

◇︰ تخطي : لتخطي الأغنية الحالية .

◇︰ ايقاف : لايقاف تشغيل الأغنية الحالية .**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/w_4_m"),
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/p_t_i"),
                ],
                [
                   InlineKeyboardButton(
                        "‹ المطور ›", url=f"https://t.me/p_t_i"),
                ],       
            ]
        ),
    )

@app.on_message(
    command(["","‹ اوامر التفعيل ›"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/7f1402824c0c70c91fd81.jpg",
        caption=f"""**
- اوامر التفعيل اتبع مايلي

— — — — — — — — — —

‹ طريقه تفعيل البوت في الكروبات والقنوات ⤈ ›

اضف البوت مع كامل الصلاحيات عدا البقاء متخفي 

افتح اتصال في المجموعة او القناة 

اكتب تشغيل + اسم الأغنية 

- سيتم انضمام الحساب المساعد الى المحادثة الصوتية وتشغيل الاغنية التي اردتها .
- الحساب المساعد عبارة عن حساب وهمي وضيفته فقط تشغيل الموسيقى 

- لاتقم بطرده او حضره اثناء تشغيل الموسيقى يمكنك استخدام الامر

- ايقاف لانهاء تشغيل المقطع الصوتي وخروج الحساب المساعد دون مشاكل**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/w_4_m"),
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/p_t_i"),
                ],
                [
                   InlineKeyboardButton(
                        "‹ المطور ›", url=f"https://t.me/p_t_i"),
                ],       
            ]
        ),
    )

@app.on_message(
    command(["",""])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/7f1402824c0c70c91fd81.jpg",
        caption=f"""**
-  اوامر التسليه
 — — — — — — — — — — 
 
- ( غنيلي ) يرسل لك اغنية عشوائية

- ( فيلم ) فيلم كامل عشوائي

- ( متحركة ) متحركات عشوائيه مميزة

- ( اقتباسات ) اقتباس بالصورة جميل

- ( اسمي ) لعرض اسمك الكامل

- ( ا ) لعرض معلوماتك

- ( تاك ) لعمل تاك جماعي في المجموعه

- لو خيروك ↫ لعبة لو خيروك

- كت تويت ↫ لعبة كت تويت عشوائي 

- صراحه ↫ لعبة صراحه

- اسئلة ↫ اسئلة عشوائيه
— — — — — — — — — — — — — —**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/w_4_m"),
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/p_t_i"),
                ],
                [
                   InlineKeyboardButton(
                        "‹ المطور ›", url=f"https://t.me/p_t_i"),
                ],       
            ]
        ),
    )
