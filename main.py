import time
from lichess_api import fetch_lichess_activity, fetch_current_game, fetch_user_profile
from discord_rpc import connect_rpc, update_presence
from config import UPDATE_INTERVAL, LICHESS_USERNAME

def format_time_control(time_control):

    if '+' in time_control: 
        base_time, increment = time_control.split('+')
        base_minutes = int(base_time) // 60
        increment_seconds = int(increment)
        return f"{base_minutes} + {increment_seconds}"
    elif time_control.isdigit(): 
        base_minutes = int(time_control) // 60
        return f"{base_minutes}"
    else:
        return "Unknown"

def main():
    rpc = connect_rpc()
    if not rpc:
        print("Failed to connect to Discord RPC. Exiting.")
        return

    print("Connected to Discord RPC.")

    previous_puzzle_rating = None  

    while True:
        current_game = fetch_current_game()
        user_profile = fetch_user_profile(LICHESS_USERNAME)

        if current_game:

            white = current_game.get("white", "Unknown")
            black = current_game.get("black", "Unknown")
            time_control = current_game.get("time_control", "Unknown")


            formatted_time_control = format_time_control(time_control)


            if "lichess AI" in white or "lichess AI" in black:
                ai_level = white.split("level")[1] if "lichess AI" in white else black.split("level")[1]
                update_presence(
                    rpc,
                    state=f"Playing Stockfish Level {ai_level}",
                    details=f"Training Against AI",
                )
            else:

                opponent = white if black == LICHESS_USERNAME else black
                update_presence(
                    rpc,
                    state=f"Playing against {opponent}",
                    details=f"Time Control: {formatted_time_control}",
                )
        elif user_profile and "perfs" in user_profile and "puzzle" in user_profile["perfs"]:

            current_puzzle_rating = user_profile["perfs"]["puzzle"]["rating"]

            if current_puzzle_rating != previous_puzzle_rating:
                previous_puzzle_rating = current_puzzle_rating
                update_presence(
                    rpc,
                    state="Solving Puzzles",
                    details=f"Puzzle Rating: {current_puzzle_rating}",
                )
            else:
                update_presence(
                    rpc,
                    state="Browsing Lichess",
                    details=f"{LICHESS_USERNAME}",
                )
        else:

            update_presence(
                rpc,
                state="Browsing Lichess",
                details=f"{LICHESS_USERNAME}",
            )

        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
