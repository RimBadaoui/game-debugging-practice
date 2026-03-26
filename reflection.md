# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The hints were backwards and the score calculation was unusual. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project? - I used Claude Code
- correct AI suggestion: moved the core logic from app.py to logic utils and updated the imports in app.py correctly. I verified by ensuring it didn't change the actual logic (the functions) and imported all the necessary function in logic_utils.py. I also verified by testing the game and seeing it work with the correct logic.
- incorrect AI suggestion: the only incorrect/misleading AI suggestions I received were copilot's attempts to autocomplete my comments. I knew it was incorrect because it incorrectly described the code I was describing.

---

## 3. Debugging and testing your fixes

- I tested it myself by playing the game and also by asking Claude Code to make a pytest. Each of my tests targetted a specific bug and I tested with several different inputs and in different orders and numbers of attempts to ensure the bug no longer occured and the correct thing happened instead. 
- I tested the too high/low alert by asking Claude Code to make a pytest to test that bug. It set the secret to 10 and the guess to 9 and asserted that the outcome was "too low." The first time it ran, it failed, which showed me that the program alerted a specific one on every even attempt regardless of the true value. The part I had fixed hadn't address that part. 
- Yes, it helped me design tests for winning conditions to see if it would consider a win as a mistake depending on how many attempts I had made before. 

---

## 4. What did you learn about Streamlit and state?

- Every time you interact with the page (click a button/type something/etc.) it reruns the python script. Rerunning the script involves resetting the value of every variable, including the secret.
- Imagine every time you interact with the page — click a button, type something, move a slider — Streamlit reruns your entire Python script from top to bottom, like hitting refresh. There's no persistent connection keeping state alive; it just re-executes everything. The problem is that normal Python variables reset on every rerun. If you stored the score in a regular variable, it'd go back to 0 every time the user clicked anything.
  Session state is the fix to this. It's a dictionary 
that Streamlit keeps alive between reruns for that user's session. Anything you put in there survives the re-execution.

- I set st.session_state.secret to a random number only at the beginning of each game. 

---

## 5. Looking ahead: your developer habits

- I want to start utilizing AI to fix one bug at a time instead of all at once so I can check each fix before moving on the way I did for this assignment.
- I was a little reluctant at first to ask Claude to find the bug in the code that I had identified from playing the game because I'm used to searching for bugs on my own. Next time, I will be less hesitant to use it, especially when I know what I'm looking for. 
- This project gave me my first successful experience with AI running bash commands, which it did when running the pytest. I appreciate that capability that it has and hope to utilize it more in the future.  

NOTE: There was a large gap between the times I worked on this project. I made a good amount of progress when it was first released but then did not work on it for the next few weeks due to personal reasons I have discussed with staff. I apologize if there appear to be any discrepancies in my memory of some parts in this reflection, as I filled it out towards the end as I was finishing it up. Going forward, I will reflect as I go (I'm not used to reflecting while coding but will adapt). I appreciate your understanding. 
                            
 ╱|、
(˚ˎ 。7  
 |、˜〵          
 じしˍ,)ノ