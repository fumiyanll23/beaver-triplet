### Compute Z:=X*Y over Finite Ring by (n, n) Beaver Triple (1992).

import numpy as np

CONST = 255

def main():
  ### input
  order = int(input('The order of the finite ring: ')) # modulo number
  party = int(input('The number of participants: ')) # number of participants
  row_X, column_X = map(int, input('The number of rows of matrix X (space) the number of columns of matrix X: ').split()) # number of rows and columns of matrix X
  row_Y, column_Y = map(int, input('The number of rows of matrix Y (space) the number of columns of matrix Y: ').split()) # number of rows and columns of matrix Y
  X = np.array([list(map(int, input('Matrix X: ').split())) for _ in range(row_X)])
  Y = np.array([list(map(int, input('Matrix Y: ').split())) for _ in range(row_Y)])

  ### preprocess
  ## initialize A, B, and C
  A = np.random.randint(0, CONST, (row_X, column_X)) # shape of A is equal to shape of X
  B = np.random.randint(0, CONST, (row_Y, column_Y)) # shape of B is equal to shape of Y
  C = A @ B # C := A*B, and shape of C is equal to shape of Z

  ## make n shares
  sX = []
  sY = []
  sA = []
  sB = []
  sC = []
  for _ in range(party-1):
    sX.append(np.random.randint(0, CONST, (row_X, column_X)))
    sY.append(np.random.randint(0, CONST, (row_Y, column_Y)))
    sA.append(np.random.randint(0, CONST, (row_X, column_X)))
    sB.append(np.random.randint(0, CONST, (row_Y, column_Y)))
    sC.append(np.random.randint(0, CONST, (row_X, column_Y)))
  sX.append(X - sum(sX))
  sY.append(Y - sum(sY))
  sA.append(A - sum(sA))
  sB.append(B - sum(sB))
  sC.append(C - sum(sC)) # sum(<SHARE>) == <MATRIX>

  ### compute
  ## compute X' := sum(s(X-A))
  XX = np.zeros((row_X, column_X))
  for i in range(party):
    XX += sX[i] - sA[i]
  ## compute Y' := sum(s(Y-B))
  YY = np.zeros((row_Y, column_Y))
  for i in range(party):
    YY += sY[i] - sB[i]
  ## make n shares of Z := X*Y
  sZ = []
  sZ.append(XX@YY + XX@sB[0] + sA[0]@YY + sC[0])
  for i in range(1, party):
    sZ.append(XX@sB[i] + sA[i]@YY + sC[i])
  ## compute Z
  Z = sum(sZ)
  Z = np.mod(Z, order)
  ZZ = np.mod(X@Y, order)

  ### output
  if np.all(Z) == np.all(ZZ):
    print('Success ;)')
    print('X*Y')
    print('= Z')
    print('=', Z)
  else:
    print('Fault :(')
    print('X*Y')
    print('=', ZZ)
    print('Z')
    print('=', Z)

if __name__ == "__main__":
    main()
