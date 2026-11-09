import time
import subprocess
from pypresence import Presence

CLIENT_ID = ''

def get_update_count():
    try:
        result = subprocess.run(["checkupdates"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        lines = [line for line in result.stdout.splitlines() if line.strip()]
        return len(lines)
    except Exception:
        return 0

try:
    print("Connecting to Discord RPC...")
    rpc = Presence(CLIENT_ID)
    rpc.connect()
    rpc_buttons = [
        {"label": "CachyOS", "url": "https://cachyos.org"},
        {"label": "RPC Repo", "url": "https://github.com/LHBlitz/Cachy-Updater-Discord-RPC"}
    ]

    rpc.update(
        details="CachyOS Maintenance",
        state="Checking for updates...",
        large_image="cachyos_logo",
        large_text="CachyOS",
        small_image="arch_logo",
        small_text="Arch Linux",
        buttons=rpc_buttons
    )

    count = get_update_count()
    state_msg = f"Updating {count} packages..." if count > 0 else "System up to date"

    rpc.update(
        details="Updating CachyOS",
        state=state_msg,
        start=int(time.time()),
        large_image="cachyos_logo",
        large_text="CachyOS",
        small_image="arch_logo",
        small_text="Arch Linux",
        buttons=rpc_buttons
    )
    print(f"Discord RPC active: {state_msg}")

    subprocess.run(["arch-update"])

    rpc.update(
        details="CachyOS Maintenance",
        state="Finished updates",
        large_image="cachyos_logo",
        large_text="CachyOS",
        small_image="arch_logo",
        small_text="Arch Linux",
        buttons=rpc_buttons
    )

    time.sleep(10)
    rpc.close()

except Exception as e:
    print(f"RPC Error: {e}")
    subprocess.run(["arch-update"])
