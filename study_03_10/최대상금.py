import sys
sys.stdin = open("input.txt", "r")

T = int(input())
li2 = []
for tc in range(1, 1+T):
  li, cnt = map(str, input().split())
  for n in li:
    li2.append(n)
    
  

 print(li2)