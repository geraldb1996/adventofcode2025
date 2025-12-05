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

    print(f"{'Line':<30} | {'Max Num':<15}")
    print("-" * 41)

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Find the largest 12-digit subsequence
        k = 12
        if len(line) < k:
            print(f"{line[:27]:<30} | {'Too short':<15}")
            continue

        drop = len(line) - k
        stack = []
        
        for digit in line:
            while drop > 0 and stack and stack[-1] < digit:
                stack.pop()
                drop -= 1
            stack.append(digit)
        
        # If we still have characters to drop (e.g. decreasing sequence), truncate from end
        result_digits = stack[:k]
        max_num = int("".join(result_digits))
        
        total_sum_of_sums += max_num
        
        # Truncate line for display if too long
        display_line = (line[:27] + '...') if len(line) > 30 else line
        print(f"{display_line:<30} | {max_num:<15}")

    print("-" * 41)
    print(f"Suma de todos los números máximos: {total_sum_of_sums}")

if __name__ == "__main__":
    solve()
