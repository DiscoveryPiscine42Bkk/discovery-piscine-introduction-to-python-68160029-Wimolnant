import sys
if len(sys.argv) != 3:
    print("none")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result_range = range(num1, num2 + 1)
        print(list(result_range))
        
    except ValueError:
        pass