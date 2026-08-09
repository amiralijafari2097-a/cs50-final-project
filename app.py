from flask import Flask, render_template, request, jsonify
import random
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_123'

STATS_FILE = 'stats.json'

def load_stats():
    if not os.path.exists(STATS_FILE):
        return {'computer_wins': 0, 'player_wins': 0, 'draws': 0}
    with open(STATS_FILE, 'r') as f:
        return json.load(f)

def save_stats(stats):
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f)

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for cond in win_conditions:
        if board[cond[0]] and board[cond[0]] == board[cond[1]] and board[cond[0]] == board[cond[2]]:
            return board[cond[0]]
    if '' not in board:
        return 'draw'
    return None

@app.route('/')
def index():
    stats = load_stats()
    return render_template('vs_computer.html', stats=stats)

@app.route('/move', methods=['POST'])
def make_move():
    data = request.get_json()
    board = data['board']
    
    empty_indices = [i for i, cell in enumerate(board) if cell == '']
    if not empty_indices:
        return jsonify({'winner': 'draw', 'board': board, 'move': None})
    
    move_index = random.choice(empty_indices)
    board[move_index] = 'O'
    
    winner = check_winner(board)
    if winner:
        stats = load_stats()
        if winner == 'X':
            stats['player_wins'] += 1
        elif winner == 'O':
            stats['computer_wins'] += 1
        else:
            stats['draws'] += 1
        save_stats(stats)
        return jsonify({'winner': winner, 'board': board, 'move': move_index})
    
    return jsonify({'winner': None, 'board': board, 'move': move_index})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)