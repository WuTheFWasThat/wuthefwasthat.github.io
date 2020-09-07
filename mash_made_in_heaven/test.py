
def letter2num(x):
    return ord(x.lower()) - ord('a') + 1

def rotate(x, a):
    res = ord(x.lower()) - ord('a')
    res = (res + a) % 26
    res = chr(res + ord('a'))
    if x.upper() == x:
        res = res.upper()
    return res

# print(
#     list(map(letter2num, 'leftoverplusthyme'))
# )
print(
    list(map(letter2num, 'addthymestoextras'))
)

leftovers = 'CAGVLRUPCLGOMWECD'
offsets = [
    13,
    14,
    13,
    5,
    8,
    23,
    10,
    3,
    6,
    2,
    5,
    0,
    9,
    8,
    2,
    2,
    16,
]
for (l, a) in zip(leftovers, offsets):
    print(rotate(l, a))

