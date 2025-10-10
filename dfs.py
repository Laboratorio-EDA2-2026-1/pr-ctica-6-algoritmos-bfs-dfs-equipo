


def main():
    rows=[0,0,0,0,0,0,0,0]
    columns=[0,0,0,0,0,0,0,0]
    tab =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    line = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    line2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    n = int(input())
    dfs(0,n,rows,columns,tab,line,line2)
def dfs(a,n,rows,columns,tab,line,line2):
    if a == n:
        for u in range(0,64):
                if(u%8 == 0):
                    print("\n")
                
                print(tab[u],end=" ")
        print("\n")
        return
    
    for i in range(0,8):
        for j in range(0,8):
            if rows[i] == 0 and columns[j]==0 and line[8-i+j]==0 and line2[8-j+i]==0 and a < n:
                rows[i]=1
                columns[j]=1
                tab[i*8 + j] = 1
                line[8-i+j]=1
                line2[8-j+i]=1
                dfs(a+1,n,rows,columns,tab,line,line2)
                
            else:
                continue
            rows[i]=0
            columns[j]=0
            tab[i*8 +j]=0
            line[8-i+j]=0
            line2[8-j+i]=0
            


if __name__ == "__main__":
    main()


