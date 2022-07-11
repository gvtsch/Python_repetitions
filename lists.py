if __name__ == '__main__':
    N = int(input())
    
    list = []
    
    for _ in range(N):
        s = input().split()
        if s[0] == 'print':
            print(list)
        else:
           s = s[0] + "(" + ",".join(s[1:]) + ")"
           eval("list."+s)
