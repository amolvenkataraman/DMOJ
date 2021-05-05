import sys
raw_input = sys.stdin.readline

G = raw_input()

for a in range(int(raw_input())):
    i, j = map(int, raw_input().split())
    print(G.count("G", i, j + 1))

