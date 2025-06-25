Lichess RPC by plasterdream
---

This project is quite new and I intend to make it better with more functions in the future. Also I hope to make it an extension as well so you don't have to run it client-side every time you open lichess.
---

# Instructions
**For Windows:**

- You should make sure you have installed at least a version of python. If not, go ahead and install it [here](https://www.python.org/downloads/).
- Now click the green button labeled "Code" in the top right and download as zip afterwards. 
- The folder should be in your Downloads folder. Go there, open the folder and right click somewhere. Now click "Open Command Prompt here" 
- Run `pip install -r requirements.txt`. This installs everything needed for the RPC to run. 
- Go ahead and edit `config.py` with your own username.
- Afterwards run `python main.py` and it should work.

**For Mac/Linux:**

- I believe you already know what you are doing, but still I'm writing a short guide here. You will most likely have python installed so go ahead and download the zip file.
- After extracting, go ahead and open the terminal in the file. Install requirements with the same command `pip install -r requirements.txt` .
- Don't forget to edit the `config.py ` file.
- Go ahead and run `python main.py` for RPC to start. 

.・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・..・。.・°・.

Now it might pop up Puzzles first and I know that. That's because Lichess API doesn't really provide an endpoint, so I can't extract when a user is playing Puzzles. So I allow the RPC to check whether puzzles rating has changed since the last time it checked. If yes, then it means that the user is doing puzzles and so it switches the status (couldn't think of something better tbf). So allow it 15 seconds (it's the time the RPC refreshes to check if something new has happened) to return to browsing status, or playing, or whatever you are doing. 

Thank you very much. All suggestions welcomed.
