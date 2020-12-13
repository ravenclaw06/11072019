#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677

import telethon.sync
from telethon import TelegramClient, events
from telethon.tl import types, functions
import os
from config import Development as Config


# https://t.me/TelethonChat/13265
client = TelegramClient(input("@ohkkkkk"), Config.2241053, Config.62dc0f66e5c8cc98bba182c99f4c4f59).start()


def progress(current, total):
  print("Downloaded: " + str(current) + " of " + str(total) + " Percent: " + str((current / total) * 100))


spechide = client.get_me()
print(spechide.stringify())
# client.send_message(spechide, "Dummy Message to get active session")


"""Interactive client to test various things
"""
if __name__ == "__main__":
  """@client.on(events.NewMessage)
  def myeventhandler(event):
    print(event.raw_text)"""
  print("Loaded")
  # client.run_until_disconnected()
