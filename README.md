# telegram_bot_chinese
to run the file on windows open PowerShell
1: cd ~\Desktop
2:mkdir "telegram bot"
3:cd "telegram bot"
4: python -m venv bot_env
5. pip install python-telegram-bot deep-translator pytesseract pillow pyautogui
6. cd ~\Desktop\"telegram bot"; bot_env\Scripts\activate; python my_bot.py
for mac open terminal
cd ~/Desktop && mkdir -p "telegram bot" && cd "telegram bot"
python3 -m venv bot_env
source bot_env/bin/activate && pip install --upgrade pip && pip install python-telegram-bot deep-translator Pillow pytesseract pyautogui httpx
cd ~/Desktop/"telegram bot" && source bot_env/bin/activate && python my_bot.py
