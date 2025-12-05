def solve():
    import os
    try:
        # Use absolute path relative to script location for robustness
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'dia3_input.txt')
        
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: dia3_input.txt not found.")
        return

    total_sum_of_sums = 0

    print(f"{'Line':<30} | {'Max Num':<8}")
    print("-" * 41)

    for line in lines:
        line = line.strip()
        if not line:
            continue

        max_num = -1
        best_pair = (0, 0)

        # Iterate through all pairs (i, j) with i < j
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                # Form the number
                num_str = line[i] + line[j]
                num = int(num_str)
                
                if num > max_num:
                    max_num = num
                    best_pair = (int(line[i]), int(line[j]))
        
        
        total_sum_of_sums += max_num
        
        # Truncate line for display if too long
        display_line = (line[:27] + '...') if len(line) > 30 else line
        print(f"{display_line:<30} | {max_num:<8}")

    print("-" * 41)
    print(f"Suma de todos los números máximos: {total_sum_of_sums}")

if __name__ == "__main__":
    solve()
