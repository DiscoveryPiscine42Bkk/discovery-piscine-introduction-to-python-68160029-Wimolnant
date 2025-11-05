import sys
if len(sys.argv) > 1:
    print("none")
else:
    N = 0
    while N <= 10:
        output_line = f"Table de {N}:"
        results = []
        i = 0
        while i <= 10:
            result = N * i
            results.append(str(result))
            i += 1
        if N == 0:
            output_line += "".join(results)
        else:
            output_line += " " + " ".join(results)
        print(output_line)
        N += 1