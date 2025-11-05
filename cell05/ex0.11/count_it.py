import sys
parameters_list = sys.argv[1:]
num_parameters = len(parameters_list)
if num_parameters == 0:
    print("none")
else:
    print(f"parameters: {num_parameters}")
    for param in parameters_list:
        param_length = len(param)
        
        print(f"{param}: {param_length}")