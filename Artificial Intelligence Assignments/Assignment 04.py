{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CQ-Gda5qof9g",
        "outputId": "dab315bf-b2be-4d73-d8ec-17aae9f002a3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The destination cell is found\n",
            "The Path is \n",
            "-> (8, 0) -> (7, 0) -> (6, 0) -> (5, 0) -> (4, 1) -> (3, 2) -> (2, 1) -> (1, 0) -> (0, 0) \n"
          ]
        }
      ],
      "source": [
        "# Python program for A* Search Algorithm\n",
        "import math\n",
        "import heapq\n",
        "\n",
        "# Define the Cell class\n",
        "\n",
        "\n",
        "class Cell:\n",
        "    def __init__(self):\n",
        "      # Parent cell's row index\n",
        "        self.parent_i = 0\n",
        "    # Parent cell's column index\n",
        "        self.parent_j = 0\n",
        " # Total cost of the cell (g + h)\n",
        "        self.f = float('inf')\n",
        "    # Cost from start to this cell\n",
        "        self.g = float('inf')\n",
        "    # Heuristic cost from this cell to destination\n",
        "        self.h = 0\n",
        "\n",
        "\n",
        "# Define the size of the grid\n",
        "ROW = 9\n",
        "COL = 10\n",
        "\n",
        "# Check if a cell is valid (within the grid)\n",
        "\n",
        "\n",
        "def is_valid(row, col):\n",
        "    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)\n",
        "\n",
        "# Check if a cell is unblocked\n",
        "\n",
        "\n",
        "def is_unblocked(grid, row, col):\n",
        "    return grid[row][col] == 1\n",
        "\n",
        "# Check if a cell is the destination\n",
        "\n",
        "\n",
        "def is_destination(row, col, dest):\n",
        "    return row == dest[0] and col == dest[1]\n",
        "\n",
        "# Calculate the heuristic value of a cell (Euclidean distance to destination)\n",
        "\n",
        "\n",
        "def calculate_h_value(row, col, dest):\n",
        "    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5\n",
        "\n",
        "# Trace the path from source to destination\n",
        "\n",
        "\n",
        "def trace_path(cell_details, dest):\n",
        "    print(\"The Path is \")\n",
        "    path = []\n",
        "    row = dest[0]\n",
        "    col = dest[1]\n",
        "\n",
        "    # Trace the path from destination to source using parent cells\n",
        "    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):\n",
        "        path.append((row, col))\n",
        "        temp_row = cell_details[row][col].parent_i\n",
        "        temp_col = cell_details[row][col].parent_j\n",
        "        row = temp_row\n",
        "        col = temp_col\n",
        "\n",
        "    # Add the source cell to the path\n",
        "    path.append((row, col))\n",
        "    # Reverse the path to get the path from source to destination\n",
        "    path.reverse()\n",
        "\n",
        "    # Print the path\n",
        "    for i in path:\n",
        "        print(\"->\", i, end=\" \")\n",
        "    print()\n",
        "\n",
        "# Implement the A* search algorithm\n",
        "\n",
        "\n",
        "def a_star_search(grid, src, dest):\n",
        "    # Check if the source and destination are valid\n",
        "    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):\n",
        "        print(\"Source or destination is invalid\")\n",
        "        return\n",
        "\n",
        "    # Check if the source and destination are unblocked\n",
        "    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):\n",
        "        print(\"Source or the destination is blocked\")\n",
        "        return\n",
        "\n",
        "    # Check if we are already at the destination\n",
        "    if is_destination(src[0], src[1], dest):\n",
        "        print(\"We are already at the destination\")\n",
        "        return\n",
        "\n",
        "    # Initialize the closed list (visited cells)\n",
        "    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]\n",
        "    # Initialize the details of each cell\n",
        "    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]\n",
        "\n",
        "    # Initialize the start cell details\n",
        "    i = src[0]\n",
        "    j = src[1]\n",
        "    cell_details[i][j].f = 0\n",
        "    cell_details[i][j].g = 0\n",
        "    cell_details[i][j].h = 0\n",
        "    cell_details[i][j].parent_i = i\n",
        "    cell_details[i][j].parent_j = j\n",
        "\n",
        "    # Initialize the open list (cells to be visited) with the start cell\n",
        "    open_list = []\n",
        "    heapq.heappush(open_list, (0.0, i, j))\n",
        "\n",
        "    # Initialize the flag for whether destination is found\n",
        "    found_dest = False\n",
        "\n",
        "    # Main loop of A* search algorithm\n",
        "    while len(open_list) > 0:\n",
        "        # Pop the cell with the smallest f value from the open list\n",
        "        p = heapq.heappop(open_list)\n",
        "\n",
        "        # Mark the cell as visited\n",
        "        i = p[1]\n",
        "        j = p[2]\n",
        "        closed_list[i][j] = True\n",
        "\n",
        "        # For each direction, check the successors\n",
        "        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),\n",
        "                      (1, 1), (1, -1), (-1, 1), (-1, -1)]\n",
        "        for dir in directions:\n",
        "            new_i = i + dir[0]\n",
        "            new_j = j + dir[1]\n",
        "\n",
        "            # If the successor is valid, unblocked, and not visited\n",
        "            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:\n",
        "                # If the successor is the destination\n",
        "                if is_destination(new_i, new_j, dest):\n",
        "                    # Set the parent of the destination cell\n",
        "                    cell_details[new_i][new_j].parent_i = i\n",
        "                    cell_details[new_i][new_j].parent_j = j\n",
        "                    print(\"The destination cell is found\")\n",
        "                    # Trace and print the path from source to destination\n",
        "                    trace_path(cell_details, dest)\n",
        "                    found_dest = True\n",
        "                    return\n",
        "                else:\n",
        "                    # Calculate the new f, g, and h values\n",
        "                    g_new = cell_details[i][j].g + 1.0\n",
        "                    h_new = calculate_h_value(new_i, new_j, dest)\n",
        "                    f_new = g_new + h_new\n",
        "\n",
        "                    # If the cell is not in the open list or the new f value is smaller\n",
        "                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:\n",
        "                        # Add the cell to the open list\n",
        "                        heapq.heappush(open_list, (f_new, new_i, new_j))\n",
        "                        # Update the cell details\n",
        "                        cell_details[new_i][new_j].f = f_new\n",
        "                        cell_details[new_i][new_j].g = g_new\n",
        "                        cell_details[new_i][new_j].h = h_new\n",
        "                        cell_details[new_i][new_j].parent_i = i\n",
        "                        cell_details[new_i][new_j].parent_j = j\n",
        "\n",
        "    # If the destination is not found after visiting all cells\n",
        "    if not found_dest:\n",
        "        print(\"Failed to find the destination cell\")\n",
        "\n",
        "# Driver Code\n",
        "\n",
        "\n",
        "def main():\n",
        "    # Define the grid (1 for unblocked, 0 for blocked)\n",
        "    grid = [\n",
        "        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],\n",
        "        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],\n",
        "        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],\n",
        "        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],\n",
        "        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],\n",
        "        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],\n",
        "        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],\n",
        "        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],\n",
        "        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]\n",
        "    ]\n",
        "\n",
        "    # Define the source and destination\n",
        "    src = [8, 0]\n",
        "    dest = [0, 0]\n",
        "\n",
        "    # Run the A* search algorithm\n",
        "    a_star_search(grid, src, dest)\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    }
  ]
}
