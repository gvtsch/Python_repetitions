if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([score, name])
        
    records.sort()
    b = [i for i in records if i[0] != records[0][0]]
    c = [i for i in b if i[0] == b[0][0]]
    
    c.sort(key=lambda x: x[1])
    for i in range(len(c)):
        print(c[i][1])
