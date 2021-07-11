import sys
input = sys.stdin.readline
tc = int(input())

def check(grid):
    cnt = 0
    if (grid[0][1] + grid[2][1]) / 2 == grid[1][1]:
        cnt += 1
    if (grid[1][0] + grid[1][2]) / 2 == grid[1][1]:
        cnt += 1
    if (grid[0][0] + grid[2][2]) / 2 == grid[1][1]:
        cnt += 1
    if (grid[0][2] + grid[2][0]) / 2 == grid[1][1]:
        cnt += 1
    return cnt


for t in range(1, tc+1):
    grid = [list(map(int, input().rstrip().split())) for _ in range(3)]
    grid[1].insert(1, 0)
    cnt = 0
    for i in range(0, 3, 2):
        if (grid[i][0] + grid[i][2]) / 2 == grid[i][1]:
            cnt += 1
        if (grid[0][i] + grid[2][i]) / 2 == grid[1][i]:
            cnt += 1
    s = []
    if float.is_integer((grid[0][1] + grid[2][1]) / 2):
        grid[1][1] = (grid[0][1] + grid[2][1]) / 2
        s.append(check(grid))
    if float.is_integer((grid[1][0] + grid[1][2]) / 2):
        grid[1][1] = (grid[1][0] + grid[1][2]) / 2
        s.append(check(grid))
    if float.is_integer((grid[0][0] + grid[2][2]) / 2):
        grid[1][1] = (grid[0][0] + grid[2][2]) / 2
        s.append(check(grid))
    if float.is_integer((grid[0][2] + grid[2][0]) / 2):
        grid[1][1] = (grid[0][2] + grid[2][0]) / 2
        s.append(check(grid))
    print(f"Case #{t}: {cnt + max(s)}")