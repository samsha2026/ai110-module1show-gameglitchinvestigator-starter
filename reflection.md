# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game it looked normal but once I started playing I noticed things were off pretty quickly. The hints were completely backwards, when my guess was too high it told me to go higher and when it was too low it told me to go lower so it was impossible to actually win. The secret number was also being converted to a string on even attempts which broke the whole comparison so you could never win on those turns. The score was bugged too, it was giving you points for guessing wrong on even attempts instead of taking them away. On top of all that, logic_utils.py had no actual code in it, just errors that would crash the app if anything tried to call those functions.

---

## 2. How did you use AI as a teammate?

I used Claude to help me find the bugs, write the fixes, and generate the tests. One thing the AI got right was catching that the secret number was being turned into a string on even attempts, that was a sneaky bug that was hard to see just by reading the code and the fix worked right away. One thing I had to figure out myself was the pytest setup, the AI told me to just run pytest but it kept failing until I used PYTHONPATH=. pytest tests/ instead so I had to troubleshoot that part on my own. AI was helpful for spotting issues fast but I still had to run and test everything myself to actually know it worked.


---

## 3. Debugging and testing your fixes

I knew a bug was fixed when the game worked correctly during live play and all the pytest tests passed. I ran PYTHONPATH=. pytest tests/ and got all 9 tests passing covering things like winning, too high, too low, score updates, and bad input. AI helped me figure out what edge cases to test like empty input and non-number input which I probably would have missed on my own. Seeing all 9 tests go green was how I confirmed everything was actually working and not just looking like it worked.
---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the whole script from top to bottom every time you click anything on the page. That means if you store something in a regular variable like the secret number it just gets regenerated every rerun which is exactly why the secret kept changing. Session state is how you keep values alive between those reruns, anything stored there sticks around. It's a really different way of thinking compared to a normal Python script and I didn't expect that at first.
---


## 5. Looking ahead: your developer habits

One habit I want to keep is writing tests at the same time as fixes instead of after, it saved a lot of time being able to just run pytest and see immediately if something broke. Next time I'd be more specific with my AI prompts from the start since the more specific I was the better and faster the results were. This project changed how I think about AI code, I used to assume it was mostly fine but now I know you have to actually read it, run it, and test it just like any other code before you trust it.

---