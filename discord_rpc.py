from pypresence import Presence
from config import DISCORD_CLIENT_ID

# Connect to Discord RPC
def connect_rpc():
    try:
        rpc = Presence(DISCORD_CLIENT_ID)
        rpc.connect()
        return rpc
    except Exception as e:
        print(f"Error connecting to Discord RPC: {e}")
        return None

def update_presence(rpc, state, details, large_image="lichess_logo", large_text="Lichess.org"):
    """Update Discord Rich Presence."""
    try:
        rpc.update(
            state=state,
            details=details
        )
    except Exception as e:
        print(f"Error updating Discord presence: {e}")
