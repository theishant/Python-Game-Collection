{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ee4c469a-d47e-4434-b2d3-618fa1c4684c",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "grid = []\n",
    "line = []\n",
    "for i in range (3):\n",
    "    for j in range (3):\n",
    "        line.append(\" \")\n",
    "    grid.append(line)\n",
    "    line = []\n",
    " \n",
    "\n",
    "def print_grid():\n",
    "    for i in range(3):\n",
    "        print(\"|\", end =\"\")\n",
    "        for j in range(3):\n",
    "            print (grid[i][j], \"|\", end =\"\")\n",
    "        print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a7d1ab4d-2734-421d-ba91-38bb503ae330",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def player_turn(turn_player1):\n",
    "    if turn_player1 == True:\n",
    "        turn_player1 = False\n",
    "        print(f\"It's {player2}'s turn\")\n",
    "    else:\n",
    "        turn_player1 = True\n",
    "        print(f\"It's {player1}'s turn\")        \n",
    "    return turn_player1\n",
    " \n",
    "\n",
    "def write_cell(cell):\n",
    "    cell -= 1\n",
    "    i = int(cell / 3)\n",
    "    j =  cell % 3   \n",
    "    if turn_player1 == True:\n",
    "        grid[i][j] = player1_symbol\n",
    "    else:\n",
    "        grid[i][j] = player2_symbol\n",
    "    return grid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "1f89d170-711d-4714-ae5d-c0c144215398",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def free_cell(cell):\n",
    "    cell -= 1\n",
    "    i = int(cell / 3)\n",
    "    j =  cell % 3\n",
    "    if grid[i][j] == player1_symbol or grid[i][j] == player2_symbol:\n",
    "        print(\"This cell is not free\")\n",
    "        return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "15b9a482-9f72-42ef-a287-b0443e9b4730",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the Tic-Tac-Toe !\n",
      "\n",
      "|  |  |  |\n",
      "|  |  |  |\n",
      "|  |  |  |\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter name of player 1 :  ishant\n",
      "Please enter the symbol of player 1 :  X\n",
      "Please enter name of player 2 :  WYZ\n",
      "Please enter the symbol of player 2 :  Y\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(\"Welcome to the Tic-Tac-Toe !\")\n",
    "print(\"\")\n",
    "print_grid()\n",
    "print(\"\")\n",
    "player1 = input(\"Please enter name of player 1 : \")\n",
    "player1_symbol = input(\"Please enter the symbol of player 1 : \")\n",
    "player2 = input(\"Please enter name of player 2 : \")\n",
    "player2_symbol = input(\"Please enter the symbol of player 2 : \")\n",
    "game = True\n",
    "full_grid = False\n",
    "turn_player1 = False\n",
    "winner = \"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ca00ca6f-2631-49cc-bf91-d176b21798da",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def win_check(grid, player1_symbol, player2_symbol):\n",
    "    full_grid = True\n",
    "    player1_symbol_count = 0\n",
    "    player2_symbol_count = 0\n",
    "    #checking rows    \n",
    "    for i in range(3):\n",
    "        for j in range(3):\n",
    "            if grid[i][j] == player1_symbol:\n",
    "                player1_symbol_count += 1\n",
    "                player2_symbol_count = 0\n",
    "                if player1_symbol_count == 3:\n",
    "                    game = False\n",
    "                    winner = player1\n",
    "                    return game, winner\n",
    "            if grid[i][j] == player2_symbol:\n",
    "                player2_symbol_count += 1\n",
    "                player1_symbol_count = 0\n",
    "                if player2_symbol_count == 3:\n",
    "                    game = False\n",
    "                    winner = player2\n",
    "                    return game, winner\n",
    "            if grid[i][j] == \" \":\n",
    "                full_grid = False\n",
    "                 \n",
    "        player1_symbol_count = 0\n",
    "        player2_symbol_count = 0\n",
    "    \n",
    "    player1_symbol_count = 0\n",
    "    player2_symbol_count = 0    \n",
    "    for i in range (3):\n",
    "        for j in range (3):\n",
    "            for k in range (3):\n",
    "                if i + k <= 2:\n",
    "                    if grid[i + k][j] == player1_symbol:\n",
    "                        player1_symbol_count += 1\n",
    "                        player2_symbol_count = 0\n",
    "                        if player1_symbol_count == 3:\n",
    "                            game = False\n",
    "                            winner = player1\n",
    "                            return game, winner\n",
    "                    if grid[i + k][j] == player2_symbol:\n",
    "                        player2_symbol_count += 1\n",
    "                        player1_symbol_count = 0\n",
    "                        if player2_symbol_count == 3:\n",
    "                            game = False\n",
    "                            winner = player2\n",
    "                            return game, winner\n",
    "            if grid[i][j] == \" \":\n",
    "                full_grid = False\n",
    " \n",
    "            player1_symbol_count = 0\n",
    "            player2_symbol_count = 0\n",
    "   \n",
    "    player1_symbol_count = 0\n",
    "    player2_symbol_count = 0    \n",
    "    for i in range (3):\n",
    "        for j in range (3):\n",
    "            for k in range (3):\n",
    "                if j + k <= 2 and i + k <= 2:\n",
    "                    if grid[i + k][j + k] == player1_symbol:\n",
    "                        player1_symbol_count += 1\n",
    "                        player2_symbol_count = 0\n",
    "                        if player1_symbol_count == 3:\n",
    "                            game = False\n",
    "                            winner = player1\n",
    "                            return game, winner\n",
    "                    if grid[i + k][j + k] == player2_symbol:\n",
    "                        player2_symbol_count += 1\n",
    "                        player1_symbol_count = 0\n",
    "                        if player2_symbol_count == 3:\n",
    "                            game = False\n",
    "                            winner = player2\n",
    "                            return game, winner\n",
    "            if grid[i][j] == \" \":\n",
    "                full_grid = False\n",
    "             \n",
    "            player1_symbol_count = 0\n",
    "            player2_symbol_count = 0\n",
    "             \n",
    "    player1_symbol_count = 0\n",
    "    player2_symbol_count = 0    \n",
    "    for i in range (3):\n",
    "        for j in range (3):\n",
    "            for k in range (3):\n",
    "                if j - k >= 0 and i + k <= 2:\n",
    "                    if grid[i + k][j - k] == player1_symbol:\n",
    "                        player1_symbol_count += 1\n",
    "                        player2_symbol_count = 0\n",
    "                        if player1_symbol_count == 3:\n",
    "                            game = False\n",
    "                            winner = player1\n",
    "                            return game, winner\n",
    "                    if grid[i + k][j - k] == player2_symbol:\n",
    "                        player2_symbol_count += 1\n",
    "                        player1_symbol_count = 0\n",
    "                        if player2_symbol_count == 3:\n",
    "                            game = False\n",
    "                            winner = player2\n",
    "                            return game, winner\n",
    "            if grid[i][j] == \" \":\n",
    "                full_grid = False\n",
    "         \n",
    "            player1_symbol_count = 0\n",
    "            player2_symbol_count = 0              \n",
    "         \n",
    "    \n",
    "    if full_grid == True:\n",
    "        game = False\n",
    "        winner = \"\"\n",
    "        return game, winner\n",
    "    else:\n",
    "        game = True\n",
    "        winner = \"\"\n",
    "        return game, winner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2ace796e-e371-47d0-adba-206ccf898f12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It's ishant's turn\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter a number for your case (1 to 9 from left to right and from top to bottom) :  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "|  |  |X |\n",
      "|  |  |  |\n",
      "|  |  |  |\n",
      "It's WYZ's turn\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter a number for your case (1 to 9 from left to right and from top to bottom) :  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "|  |  |X |\n",
      "|  |Y |  |\n",
      "|  |  |  |\n",
      "It's ishant's turn\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter a number for your case (1 to 9 from left to right and from top to bottom) :  6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "|  |  |X |\n",
      "|  |Y |X |\n",
      "|  |  |  |\n",
      "It's WYZ's turn\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter a number for your case (1 to 9 from left to right and from top to bottom) :  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "|Y |  |X |\n",
      "|  |Y |X |\n",
      "|  |  |  |\n",
      "It's ishant's turn\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter a number for your case (1 to 9 from left to right and from top to bottom) :  9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "|Y |  |X |\n",
      "|  |Y |X |\n",
      "|  |  |X |\n",
      "Winner is ishant !\n"
     ]
    }
   ],
   "source": [
    "\n",
    "while game == True:\n",
    "    turn_player1 = player_turn(turn_player1)\n",
    "    free_box = False\n",
    "    while free_box == False:\n",
    "        cell = int(input(\"Please enter a number for your case (1 to 9 from left to right and from top to bottom) : \"))\n",
    "        free_box = free_cell(cell)\n",
    "    grid = write_cell(cell)\n",
    "    print_grid()\n",
    "    game, winner = win_check(grid, player1_symbol, player2_symbol)\n",
    "     \n",
    "\n",
    "if winner == player1:\n",
    "    print(f\"Winner is {player1} !\")\n",
    "elif winner == player2:\n",
    "    print(f\"Winner is {player2} !\")\n",
    "else:\n",
    "    print(f\"Grid is full : equality for {player1} and {player2} !\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32672533-2537-4508-a06a-4e4eb7b65ff2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
