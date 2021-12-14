def main():
    # used dictionary to store results
    ans = {1:[],2:[],3:[],4:[],5:[]}

    for num in range(1,101):
        # numbers that are divisible by 7 and 3
        if num%7 == 0 and num%3 == 0:
            ans[1].append(num)
        
        # numbers that are divisible by 7 but not 3
        if num%7 == 0 and num%3 != 0:
            ans[2].append(num)
        
        # ODD numbers divisible by 7 but not 3
        if num%2 != 0 and num%7 == 0 and num%3 != 0:
            ans[3].append(num)
        
        # numbers that are divisible by the sum of its digits
        digit_total = 0
        for digit in str(num):
            digit_total += int(digit)
    
        if num%digit_total == 0:
            ans[4].append(num)
        
        # numbers that are equal to the square of the sum of its digits
        if num == digit_total**2:
            ans[5].append(num)

    print(f"Numbers that are divisible by 7 and 3: {ans[1]}")
    print(f"Numbers that are divisible by 7 but not 3: {ans[2]}")
    print(f"ODD numbers divisible by 7 but not 3: {ans[3]}")
    print(f"Numbers that are divisible by the sum of its digits: {ans[4]}")
    print(f"Numbers that are equal to the square of the sum of its digits: {ans[5]}")


main()
