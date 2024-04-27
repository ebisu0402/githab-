def check ():
    odd_numbers = []
    even_numbers = []
    
    for number in range(1, 101):
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers , odd_numbers

def main():
    even_numbers , odd_numbers = check()
    print("偶数:", even_numbers)  
    print("奇数:", odd_numbers)    

if __name__ == "__main__":
    main()