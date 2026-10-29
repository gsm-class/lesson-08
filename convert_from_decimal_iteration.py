# 30 2
# 15 ... 0
# 7 ... 1
# 3 ... 1
# 1 ... 1
# 0 ... 1

n, b = map(int, input().split())

result_list = []
q = n

# char_map_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while q > 0:
    # r = q % b
    # q = q // b
    # pass
    
    if r < 10:
        # pass
    else:
        # r-10 => 0 ~ 25
        # r-10+ord('A') => ord('A') ~ ord('Z')
        # chr(r-10+ord('A')) => 'A' ~ 'Z'

        # pass

    # result_list.append(char_map_str[r])

print("".join(result_list[::-1]) or "0")