import time
import subprocess
from pypresence import Presence

CLIENT_ID = '1561502376131694743'

try:
    print("Connecting to Discord RPC...")
    rpc = Presence(CLIENT_ID)
    rpc.connect()
    
    rpc.update(
        details="Updating CachyOS",
        state="Upgrading packages...",
        start=int(time.time()),
        large_image="cachyos_logo",
        large_text="CachyOS"
    )
    print("Discord RPC active!")
    
    subprocess.run(["arch-update"])
    
    time.sleep(3)
    rpc.close()

except Exception as e:
    print(f"RPC Error: {e}")
    subprocess.run(["arch-update"])