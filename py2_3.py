m = 4
#g = [[i + j if j < int(m/2 if m%2 == 0 else m/2 + 1) else int(m/2 - 1 + i - j%(m/2)) for j in range(m)] if i < int(m/2) else [m - i - 1 + j if j < int(m/2 if m%2 == 0 else m/2 + 1) else int(m/2 - 1 + (m - i - 1) - j%(m/2)) for j in range(m)] for i in range(m)]

g = [[i+j if (j<m/2) else (m - j - 1) + i for j in range(m)] if(i < m/2) else [(m - i - 1) + j if (j<m/2) else (m - j) + (m - i) - 2 for j in range(m)] for i in range(m)]

for i in g:
  print(i);
