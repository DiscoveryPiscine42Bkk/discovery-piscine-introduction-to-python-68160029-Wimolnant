import sys
parameters = sys.argv[1:]

if len(parameters) >= 2:
    reversed_parameters = parameters[::-1]
    
    for param in reversed_parameters:
        print(param)
else:
    print("none")