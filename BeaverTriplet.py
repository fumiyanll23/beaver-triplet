### Compute Z := X * Y over Z_4 by (2, 2) Beaver Triple (1992).

import numpy as np

def main():
  ### input
  p = 4 # modulo number
  row = 3 # number of rows
  column = 4 # number of columns
  # party = 2 # number of participants
  X = np.array([list(map(int, input().split())) for _ in range(row)])
  Y = np.array([list(map(int, input().split())) for _ in range(column)])

  ### preprocess
  ## define A, B, and C
  A = np.random.randint(0, 4, (row, column)) # type of A is (3, 4) over Z_4
  B = np.random.randint(0, 4, (column, row)) # type of B is (4, 3) over Z_4
  C = A @ B # C := A * B, and type of C is (3, 3) over F_4

  ## make shares (now, just 2 shares...)
  sX1 = np.random.randint(0, 4, (row, column))
  sX2 = X - sX1
  sY1 = np.random.randint(0, 4, (column, row))
  sY2 = Y - sY1
  sA1 = np.random.randint(0, 4, (row, column))
  sA2 = A - sA1
  sB1 = np.random.randint(0, 4, (column, row))
  sB2 = B - sB1
  sC1 = np.random.randint(0, 4, (row, row))
  sC2 = C - sC1

  ### compute
  XX = (sX1-sA1) + (sX2-sA2) # compute X'
  YY = (sY1-sB1) + (sY2-sB2) # compute Y'
  sZ1 = XX@YY + XX@sB1 + sA1@YY + sC1
  sZ2 = XX@sB2 + sA2@YY + sC2
  Z = sZ1 + sZ2
  Z = np.mod(Z, p)
  ZZ = np.mod(X@Y, p)

  ### output
  if np.all(Z) == np.all(ZZ):
    print('Success;)')
    print('X*Y')
    print('= Z')
    print('=', Z)
  else:
    print('Fault:(')
    print('X*Y')
    print('=', ZZ)
    print('Z')
    print('=', Z)

if __name__ == "__main__":
    main()
