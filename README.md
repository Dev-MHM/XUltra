# Installing Step1
First install [Termux](https://play.google.com/store/apps/details?id=com.termux)
Open it and give this commands

```
termux-setup-storage

pkg install python git -y

python3.8 -m venv venv

pip install telethon

. ./venv/bin/activate

cd /sdcard/Telegram

git clone https://github.com/Dev-MHM/XUltra.git

cd XUltra

python3 telesetup.py

```

than copy your sessionkey
# Isntallation Step2
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
