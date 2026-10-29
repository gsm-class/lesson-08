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
    q, r = divmod(q, b)
    
    if r < 10:
        result_list.append(str(r))
    else:
        # r-10 => 0 ~ 25
        # r-10+ord('A') => ord('A') ~ ord('Z')
        # chr(r-10+ord('A')) => 'A' ~ 'Z'

        result_list.append(chr(r-10+ord('A')))

    # result_list.append(char_map_str[r])

print("".join(result_list[::-1]))