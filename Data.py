from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/Skytrixsz")],
    ]

    # Help Message
    HELP = """
"""

    # About Message
    ABOUT = """
𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝘼𝘽𝙊𝙐𝙏 𝙈𝙀
𝙉𝘼𝙈𝙀 : [𝙏𝙊𝙅𝙄 𝘽𝙊𝙏](t.me/skytrixszbot)
𝙂𝙍𝙐𝙋 𝙎𝙐𝙋𝙋𝙊𝙍𝙏 : [𝙒𝙄𝘽𝙐 𝙃𝙊𝙐𝙎𝙀](t.me/wibuhouse)
𝘼𝙉𝘿 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 : [𝙎𝙆𝙔𝙏𝙍𝙄𝙓𝙎𝙕](t.me/skytrixch)
𝙊𝙒𝙉𝙀𝙍 𝙍𝙀𝙋𝙊 : [𝙄𝙆𝙄𝙎𝘼𝙉](t.me/skytrixsz)
    """
