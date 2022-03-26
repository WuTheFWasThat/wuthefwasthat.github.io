# https://docs.google.com/spreadsheets/d/1LhycSdy7j5kDBUMfT4BoFsqK6uYvqgOLgFEhxCLTyL8/edit?skip_itp2_check=true#gid=0

# VERIFYING 3 SIG FIGS IS ENOUGH
import numpy as np
h = dict()
for i in range(1, 27):
  for j in range(i+1, 27):
    val = np.log(j) - np.log(i)
    val_str = f"{val:.03f}"
    if val_str in h:
      (i2, j2) = h[val_str]
      if j2 * i == i2 * j:
        pass
      else:
        print("collision", (i, j), h[val_str])
    else:
      h[val_str] = (i, j)

import numpy as np
h = dict()
for i in range(1, 27):
  for j in range(1, 27):
    val = np.log(j) - np.log(i)
    val_str = f"{val:.03f}"
    print(i, j, val_str)


"""
XXXXXXXXXXX
XX  XXX  XX
X    X    X
X XX   XX X
X XXXXXXX X
X  XXXXX  X
XX  XXX  XX
XXX  X  XXX
XXXX   XXXX
XXXXX XXXXX
XXXXXXXXXXX
"""


table_colors = """
11111111111
33222122211
32232223223
32133233123
32113331123
32211311223
33221112233
33322122333
33332223333
33331213333
33331113333
"""

table1 = """
X R I S K E D U C T I
U S J E Y R P A U N O
P R A A A N D E L S L
E E H F U A Z L E G I
R H O N N U Z G U I K
O T O E S P L O T F E
P I H C T I A F O E L
T C P A E D O L B S Y
I E R Y O E V D R R U
M R O T H T N E A E N
A L C I U M A N I V I
"""
table = table1

print("TABLE1")

for line, cline in zip(table.strip().split("\n"), table_colors.strip().split("\n")):
  rowstr = ''
  rowstr += '<tr>'
  for col, color in zip(filter(len, line.split(' ')), cline.strip()):
    rowstr += f' <td class="color{color}">' + col + '</td>'
  rowstr += '</tr>'
  print(rowstr)



table2 = """
A G O O D I G H T K I
H T A U L N J E Y S S
E D P A A D A E A S I
A L I W I N O V T L F
F R N N F S L E N O E
F O W E R E N M E V A
E A E H A I G S I U R
C E L T O L G A R G T
T T T M T F I T E I H
I A R S R T T U M F E
O N U I O B O O E D Y
"""
table = table2

print("TABLE2")

for line, cline in zip(table.strip().split("\n"), table_colors.strip().split("\n")):
  rowstr = ''
  rowstr += '<tr>'
  for col, color in zip(filter(len, line.split(' ')), cline.strip()):
    rowstr += f' <td class="color{color}">' + col + '</td>'
  rowstr += '</tr>'
  print(rowstr)



vals = []

print("WEIGHTS")
for line1, line2 in zip(table1.strip().split("\n"), table2.strip().split("\n")):
  rowstr = ''
  rowstr += '<tr>'
  for l1, l2 in zip(line1.split(' '), line2.split(' ')):
    i = ord(l1.strip()) - ord('A') + 1
    j = ord(l2.strip()) - ord('A') + 1
    val = np.log(i) - np.log(j)
    val_str = f"{val:.03f}"
    rowstr +=' <td>' + val_str + '</td>'
    vals.append(val)
  rowstr += '</tr>'
  print(rowstr)


# import matplotlib.pyplot as plt
# plt.hist(vals)
# plt.show()

# vals = [np.log(np.random.randint(1, 26)) - np.log(np.random.randint(1, 26)) for _ in range(1000)]
# plt.hist(vals)
# plt.show()
