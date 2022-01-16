import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())

e, s, m, cnt = 1, 1, 1, 1

while True:
    if e == E and s == S and m == M:
        break
    e += 1
    s += 1
    m += 1
    cnt += 1

    # E는 15, S는 28, M은 19가 최대
    if e >= 16:
        e -= 15
    if s >= 29:
        s -= 28
    if m >= 20:
        m -= 19

print(cnt)