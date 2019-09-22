# 9MensMorris

<br>

```
pip3 install -r requirements.txt
python3 main.py
```

# User Story
###### Version 1

1. As a player I need an empty board
    -  When a new game is started, there will be a 7*7 empty board consists of 3 nested squares connected by their mid points
    - Each Square has 4 vertices and 4 midpoints
    - The boards points must be empty
2. As 2 players, it has to be decided who goes first to take turns throughout the game.
    - Given the start of the game the users will be asked who goes first (white/black)
3. As players, we place pieces on empty cells.
    - Once it is a valid move place the piece
4. As a player, I want 3 pieces on a line to form a mill.
    - Given a valid turn we check if 3 of the same pieces are connected to form a mill
5. As a player, when I place 3 pieces on a row, I remove one of the opponent’s pieces. It cannot be a part of a mill unless there is no option.
6. As a player, when all pieces have been placed, I can start moving them to adjacent empty cells.
7. As a player, with only 3 pieces, I can move to any empty cell.
8. As players, we know the game is over when a player only has 2 pieces.

# Dev Info

**Adding new packages**

In requirements.txt add `{yourpackage}=={version}`

Install the package with `pip3 install -r requirements.txt`

**Using Git**

Change branch `git checkout {branch-name}`

Add changes `git add .`

Declare commit `git commit -m "{Your description}"`

Push to github `git push`

# Helpfull Links

**Python Tutorials**

[syntax](https://google.com)

[functions](https://google.com)

[classes](https://google.com)

[imports](https://google.com)

**Important Packages**

[pytest](https://google.com)

[kivy](https://google.com)

[pygame](https://google.com)