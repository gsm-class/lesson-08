# # 1)
# def convert_to_dec(q, b):
#     if q == 0:
#         return ""

#     q, r = divmod(q, b)
    
#     if r < 10:
#         char_str = str(r)
#     else:
#         char_str = chr(r-10+ord('A'))

#     return convert_to_dec(q, b) + char_str

# n, b = map(int, input().split())
# print(convert_to_dec(n, b))

# 2)

def convert_to_dec_map(q, b, char_map_str):
    if q == 0:
        return ""

    q, r = divmod(q, b)
    return convert_to_dec_map(q, b, char_map_str) + char_map_str[r]

char_map_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, input().split())
print(convert_to_dec_map(n, b, char_map_str))
