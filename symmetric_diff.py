# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()
foo = set(input().split())
_ = input()
bar = set(input().split())

print(len(foo.symmetric_difference(bar)))
