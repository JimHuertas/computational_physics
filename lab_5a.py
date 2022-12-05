
u = list()

def Laplace(ua, ub, uc, ud, n, m, h, error):
    for i in range(0, n+2):
        u[i][0] = uc
        u[0][m+2] = ud
    
    for j in range(0, n+2):
        k=j
if __name__ == "__main__":
    a=1