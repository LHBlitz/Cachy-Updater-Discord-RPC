# Cachy Updater Discord RPC

Requirements:

[CachyOS](https://cachyos.org/), [Python 3](https://www.python.org/), [PyPresence](https://pypi.org/project/pypresence/), a custom [Discord application](https://discord.com/developers/applications), and your Discord client. 

You can put this in your terminal for a quick install of PyPresence and Python 3:

```python3 -m pip install pypresence --user --break-system-packages```

Usage:

You need to create your own Discord bot so you can add it's client ID to the script. The python script should sit in your /home/user/scripts folder. The config file is made for the default "fish" shell, but should work for other shells. The directory for the config.fish file is /home/user/.config/fish/. Simply copy the contents of the config.fish file I uploaded and add it to your own config file.

The RPC should now automatically show up whenever you run ```cachy-update``` in your terminal.
