🎮 Game Glitch Investigator: The Impossible Guesser
🚨 The Situation
You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

You can't win.
The hints lie to you.
The secret number seems to have commitment issues.

🛠️ Setup

Install dependencies: pip install -r requirements.txt
Run the broken app: python -m streamlit run app.py


On Mac, use python3 instead of python. If streamlit isn't found, run:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m streamlit run app.py

🕵️‍♂️ Your Mission

Play the game. Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
Find the State Bug. Why does the secret number change every time you click "Submit"? Ask ChatGPT: "How do I keep a variable from resetting in Streamlit when I click a button?"
Fix the Logic. The hints ("Higher/Lower") are wrong. Fix them.
Refactor & Test.

Move the logic into logic_utils.py.
Run PYTHONPATH=. pytest tests/ in your terminal.
Keep fixing until all tests pass!



📝 Document Your Experience

 Game purpose: a number guessing game where you try to find the secret number within a limited number of attempts based on the difficulty you pick
 Bugs found: hints were backwards, secret number was being converted to a string on even attempts which broke comparisons, score was rewarding wrong guesses on even attempts, Hard mode range was easier than Normal, logic_utils.py had no real code just NotImplementedError placeholders
 Fixes applied: flipped the hint directions, removed the string conversion bug so the secret always stays an integer, fixed score to always subtract on wrong guesses, corrected Hard mode range to 1-200, and refactored all logic functions into logic_utils.py

📸 Demo

![Winning game](Game_glitch.png)

🚀 Stretch Features

 Added 9 automated pytest cases covering wins, losses, score updates, input parsing, and difficulty ranges