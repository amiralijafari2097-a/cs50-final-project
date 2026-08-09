# Tic-Tac-Toe vs Computer (CS50 Final Project)

#### Video Demo: [https://youtu.be/318A_jQvXsM](https://youtu.be/vfdMsAeuTY8?si=ItXeTbY9jDp8d10G)

#### Description:
This project is a web-based implementation of the classic Tic-Tac-Toe game, built as the final project for Harvard's CS50: Introduction to Computer Science. The user plays against a simple artificial intelligence (AI) opponent that moves randomly.

The goal of this project was to demonstrate full-stack web development skills, including backend logic, frontend design, and real-time interactivity using Flask, HTML, CSS, and JavaScript.

---

#### How it works:
- The game starts with the user playing as **X**.
- The computer plays as **O** and makes random moves on empty cells.
- The game automatically checks for win conditions (rows, columns, diagonals).
- If all cells are filled and no one wins, the game ends in a **Draw**.
- The game keeps track of the player's wins, computer's wins, and draws in a local JSON file (`stats.json`).
- There is a red button at the bottom of the page to **reset all statistics** to zero at any time.

---

#### Technologies Used:
- **Backend:** Python (Flask Framework)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Data Storage:** JSON file for persistent statistics
- **Deployment:** PythonAnywhere (Live web app)

---

#### How to Run Locally:
1. Clone this repository.
2. Install the dependencies: `pip install flask`
3. Run the app: `python app.py`
4. Open your browser and go to `http://127.0.0.1:5000`

---

#### Files and Folders:
- `app.py`: Main Flask application file containing the route logic and the AI logic.
- `templates/vs_computer.html`: The HTML file that renders the game board and interface.
- `static/style.css`: The CSS file responsible for the styling and layout of the game.
- `stats.json`: A JSON file used to store the persistent game statistics locally.

---

#### Future Improvements:
In the future, I would like to add a **Minimax AI algorithm** to make the computer unbeatable, and add **online multiplayer support** using WebSockets so two players can play together remotely.
