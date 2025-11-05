import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    try:
        matches = re.findall(re.escape(keyword), text)
        count = len(matches)
    except re.error:
        count = 0
        
    if count > 0:
        print(count)
    else:
        print("none")