import sys
parameters_list = sys.argv[1:]
if not parameters_list:
    print("none")
else:
    for param in parameters_list:
        if not param.endswith("ism"):
            print(param + "ism")
        