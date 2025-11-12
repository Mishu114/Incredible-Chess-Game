# Incredible Chess Game ♟️

A Python-based unique chess variant game with a graphical user interface built using Pygame. This is not your traditional chess - it's a strategic pawn-only game with special movement rules!

## 🎮 Game Rules

This is a special variant of chess with unique rules:

- **Pawns Only**: The game features only pawns, no other pieces
- **Bidirectional Movement**: Pawns can move both forward AND backward
- **Flexible Movement**: Move 1 or 2 squares in either direction per turn
- **No Captures**: You cannot capture your opponent's pawns
- **No Jumping**: You cannot jump over any pawn (yours or opponent's)
- **Win Condition**: When a player has no valid moves available, they lose the game

### Strategic Elements

- Block your opponent's pawns to limit their movement options
- Plan your moves carefully to avoid getting trapped
- Create a wall of pawns to restrict your opponent's options
- The last player with valid moves wins!

## 🎯 Features

- **Interactive GUI**: Clean and user-friendly chess board interface using Pygame
- **Custom Game Logic**: Unique movement and win condition implementation
- **AI Opponent**: Smart move finder algorithm adapted for this variant
- **Move Validation**: Automatic checking for valid moves based on custom rules
- **Visual Feedback**: Clear highlighting of valid moves

## 📁 Project Structure

```
Incredible-Chess-Game/
├── chess/
│   ├── ChessEngine.py      # Core game logic and custom rule implementation
│   ├── ChessMain.py         # Main game loop and GUI implementation
│   ├── SmartMoveFinder.py   # AI strategy for pawn-only variant
│   ├── images-chess/        # Pawn sprites and graphics
│   └── __init__.py
└── main.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Mishu114/Incredible-Chess-Game.git
cd Incredible-Chess-Game
```

2. Install the required dependencies:
```bash
pip install pygame
```

### Running the Game

```bash
python chess/ChessMain.py
```

## 🎯 How to Play

1. Launch the game using the command above
2. Click on one of your pawns to select it
3. Valid moves will be highlighted (1 or 2 squares forward or backward)
4. Click on a highlighted square to move your pawn
5. Remember: You cannot capture or jump over any pawn!
6. Play against the AI and try to trap your opponent
7. The player who runs out of valid moves loses!


## 🎲 Strategy Tips

- Try to create a solid wall of pawns to block your opponent
- Think ahead - moving forward might leave you vulnerable to being blocked
- Use the 2-square movement strategically to close gaps quickly
- Don't get trapped! Always ensure you have escape routes

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Pygame**: Graphics and game development library

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**Mishu114**
- GitHub: [@Mishu114](https://github.com/Mishu114)

## ⭐ Show your support

Give a ⭐️ if you enjoyed this project!

---

*Created with passion for chess and coding - A unique twist on a classic game!*
