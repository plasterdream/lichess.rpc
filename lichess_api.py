import requests
from config import LICHESS_ACTIVITY_URL, LICHESS_CURRENT_GAME_URL

def fetch_user_profile(username):

    try:
        response = requests.get(f"https://lichess.org/api/user/{username}")
        if response.status_code == 200:
            return response.json()
        return None
    except requests.RequestException as e:
        print(f"Error fetching user profile: {e}")
        return None

def fetch_lichess_activity():
    """Fetch user activity from Lichess."""
    try:
        response = requests.get(LICHESS_ACTIVITY_URL)
        if response.status_code == 200:
            return response.json()
        return None
    except requests.RequestException as e:
        print(f"Error fetching Lichess activity: {e}")
        return None

def fetch_current_game():

    try:
        response = requests.get(LICHESS_CURRENT_GAME_URL)

        print(f"Debug: Received status code {response.status_code} from {LICHESS_CURRENT_GAME_URL}")
        print(f"Debug: Response headers: {response.headers}")
        
        if response.status_code == 200:

            raw_pgn = response.text
            print(f"Debug: Raw PGN response content: {raw_pgn}")


            game_data = parse_pgn(raw_pgn)
            

            if game_data and "result" in game_data:
                if game_data["result"] in ["1-0", "0-1", "1/2-1/2"]: 
                    print("Game has ended, resetting to browsing status.")
                    return None  # No active game

            return game_data
        elif response.status_code == 404:
            print("Debug: No active game for the user (404 response).")
            return None
        else:
            print(f"Debug: Unexpected status code {response.status_code}. Content: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching current game: {e}")
        return None


def parse_pgn(raw_pgn):

    try:
        game_data = {}


        lines = raw_pgn.splitlines()
        for line in lines:
            if line.startswith("[White "):
                game_data["white"] = line.split('"')[1]
            elif line.startswith("[Black "):
                game_data["black"] = line.split('"')[1]
            elif line.startswith("[TimeControl "):
                game_data["time_control"] = line.split('"')[1]
            elif line.startswith("[GameId "):
                game_data["game_id"] = line.split('"')[1]
            elif line.startswith("[Result "):
                game_data["result"] = line.split('"')[1]


        return game_data if game_data else None
    except Exception as e:
        print(f"Error parsing PGN: {e}")
        return None
