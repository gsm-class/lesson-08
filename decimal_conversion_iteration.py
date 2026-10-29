#
# ZZZZZ 36
# 60466175

num_str, b = input().split()

b = int(b)
decimal_result = 0
# char_dict = {'0': 0, '1': 1, ... , 'A': 10, 'B': 11, ..., 'Z': 35}
# char_map_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(num_str)-1, -1, -1):
    # 1)
    if num_str[i].isnumeric(): # '0'~'9', 'A'~'Z'
        # pass
    else: # elif ord('A') <= ord(num_str[i]) <= ord('Z'):
        # pass

print(decimal_result)