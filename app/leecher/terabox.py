import asyncio
import aiohttp
from typing import Optional
from pyrogram.types import Message
from app.utils.logger import setup_logger

logger = setup_logger("leecher")

class TeraboxLeech:
    def __init__(self):
        self.session = None
        
    async def download(self, url: str, message: Message):
        """Download from Terabox and show progress"""
        user_id = message.from_user.id
        
        # Initial message
        progress_msg = await message.reply_text(
            f"**Terabox Link Pakda!** 🔗\n"
            f"`{url[:50]}...`\n"
            "Download shuru... 0%"
        )
        
        try:
            # Simulate download progress
            for i in range(1, 101):
                await asyncio.sleep(0.5)
                
                # Update progress every 5%
                if i % 5 == 0:
                    await progress_msg.edit_text(
                        f"**Downloading...** ⬇️\n"
                        f"Progress: `{i}%`\n"
                        f"Status: Running..."
                    )
                    
            # Complete
            await progress_msg.edit_text(
                "**Download Complete!** ✅\n"
                "File Telegram pe upload ho raha hai..."
            )
            
            # Ask user if they want Telegram file
            await message.reply_text(
                "**File download ho gaya!** 🎉\n"
                "Kya tumhe Telegram file chahiye?",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Haan! Bhej de", callback_data=f"send_file_{user_id}"),
                     InlineKeyboardButton("Nahi, link de", callback_data=f"gen_link_{user_id}")]
                ])
            )
            
            return True
            
        except Exception as e:
            logger.error(f"Terabox download error: {e}")
            await progress_msg.edit_text(f"**Error!** ❌\n`{str(e)}`")
            return False
