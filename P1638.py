def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    visit = [0] * (m + 1)
    i = 1
    j = 0
    ans_i = 1
    ans_j = n
    minn = 10000000
    cnt = 0
    while i <= n:
        while j < n and cnt < m:
            j += 1
            if visit[a[j]] == 0:
                cnt += 1
            visit[a[j]] += 1

        if cnt == m and j - i + 1 < minn:
            minn = j - i + 1
            ans_i = i
            ans_j = j

        visit[a[i]] -= 1
        if visit[a[i]] == 0:
            cnt -= 1
        i += 1

    print(ans_i, ans_j)


main()
