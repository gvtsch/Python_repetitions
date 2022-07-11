# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()
foo = set(input().split())
n = int(input())
for _ in range(n):
    cmd, _ = input().split()
    bar = set(input().split())
    eval("foo." + cmd + "(bar)")
print(sum(map(int,(foo))))
