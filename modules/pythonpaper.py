# Python3 code to program to find occurrence

inp_str = "NitishVishwakarma"
out = {x: inp_str.count(x) for x in set(inp_str)}
print("Occurrence :\n "+ str(out))
