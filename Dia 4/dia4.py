
def solve():
    import sys
    filename = 'Dia 4/inputD4.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    try:
        with open(filename, 'r') as f:
            grid = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Error: inputD4.txt not found.")
        return

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    count_isolated = 0
    
    # Directions for 8 neighbors: (row_offset, col_offset)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                neighbor_at_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check bounds
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            neighbor_at_count += 1
                
                if neighbor_at_count < 4:
                    count_isolated += 1

    print(f"Total '@' with less than 4 adjacent '@': {count_isolated}")

if __name__ == "__main__":
    solve()
