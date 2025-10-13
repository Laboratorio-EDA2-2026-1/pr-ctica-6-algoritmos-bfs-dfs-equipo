def main():

    print("Reinas: ")
    n = int(input())
    rows=[0]*n
    columns=[0]*n
    tab =[0]*(n*n)
    auxt = []
    line = [0]*(2*n)
    line2 = [0]*(2*n)
    line = [0]*(2*n)
    line2 = [0]*(2*n)
    used = [0]*n
    print("Posiciones ocupadas:")
    for i in range(0,n):
        #se debe ingresar valor por valor, no todos juntos 
        used[i] = int(input())
    print("Resultados Posibles: ")
    dfs(0,n,rows,columns,tab,line,line2,auxt,used)
    for arr in auxt:
        print(arr)

def dfs(a,n,rows,columns,tab,line,line2,auxt,used):
    
    if a == n:
        ar = [0]*n
        for u in range(n*n):
        #    if u % n == 0 and u > 0:
        #        print()
        #    print(tab[u], end=" ")
           if(tab[u] > 0): ar[u%n]= int((u/n))+1
        #print("Arreglo: ")
        #for i in ar:
        #    print(i,end=" ")
        #print("\n")
        auxt.append(ar)
    
    i = a
    for j in range(n):
        if columns[j] or line[n-1-i+j] or line2[i+j] or used[j]==i+1:
            continue

        rows[i] = columns[j] = 1
        line[n-1-i+j] = line2[i+j] = 1
        tab[i*n + j] = 1

        dfs(a+1, n, rows, columns, tab, line, line2, auxt,used)

        rows[i] = columns[j] = 0
        line[n-1-i+j] = line2[i+j] = 0
        tab[i*n + j] = 0

    
            
            


if __name__ == "__main__":
    main()



