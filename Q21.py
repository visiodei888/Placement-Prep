s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("false")
else:
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    if sorted_s1 == sorted_s2:
        print("true")
    else:
        print("false")
