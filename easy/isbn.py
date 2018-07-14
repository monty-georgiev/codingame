#! /usr/bin/python3
n = int(input())
invalid = []

for i in range(n):
    isbn = str(input())
    isbn_sum = 0
    operator = 10
    isbn_len = len(isbn)
       
    # case 10
    if isbn_len == 10 and isbn[:isbn_len-1].isdigit(): 
        for d in range(9):
            isbn_sum += int(isbn[d]) * operator
            operator -= 1
       
        check_digit = str(11 - (isbn_sum%11))
            
        if check_digit == "10":
            check_digit = "X"
        elif check_digit == "11":
            check_digit = "0"

        if check_digit != isbn[-1]:
            invalid.append(isbn)

    # case 13
    elif isbn_len == 13 and isbn[:isbn_len-1].isdigit():
        for d in range(12):
            if d % 2 == 0:
                isbn_sum += int(isbn[d]) * 1
            else:
                isbn_sum += int(isbn[d]) * 3    
                
        check_digit = str(10 - (isbn_sum % 10))
        if check_digit == "10":
            check_digit = "0"
        if check_digit != isbn[-1]:
            invalid.append(isbn)
    else:
        invalid.append(isbn)
        continue

if invalid:
    print("{} invalid:".format(len(invalid)))
    for inv in invalid:
        print(inv)
