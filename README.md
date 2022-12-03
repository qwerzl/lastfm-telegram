# lastfm-telegram
A simple python script to show now-scrobbling artwork on Last.fm. 
***Requires python3.8+***

# How to use
1. Edit `api_id` and `api_hash` of **Telegram** in main.py
2. Edit `API_KEY` `API_SECRET` `lastfm_username` and `lastfm_password` of **lastfm** in mylast.py.
3. 
```
python3 -m pip install -r requirements.txt
python3 ./main.py
```
The script will ask for your telegram login information on its first use.
# Systemd
```
cat <<'TEXT' > /etc/systemd/system/lastfm-telegram.service
[Unit]
Description=Lastfm-telegram Daemon
After=network.target

[Install]
WantedBy=multi-user.target

[Service]
WorkingDirectory=[Directory where you put this repo]
Type=simple
User=root
ExecStart=/usr/bin/python3 ./main.py
Restart=always
TEXT
```
