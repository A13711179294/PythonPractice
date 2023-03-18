from collections import defaultdict, deque


def bfs():
    queue.append(1)
    visit[1] = 1
    nums[1] = 0
    cnt[1] = 1
    while queue:
        cur_node = queue.popleft()
        for next_node in graph[cur_node]:
            if visit[next_node] == 0:
                visit[next_node] = 1
                nums[next_node] = nums[cur_node] + 1
                queue.append(next_node)
            if nums[next_node] == nums[cur_node] + 1:
                cnt[next_node] += cnt[cur_node]
                cnt[next_node] %= 100003


graph = defaultdict(list)
queue = deque()
n, m = map(int, input().split())
visit = [0] * (n + 1)
nums = [0] * (n + 1)
cnt = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    if u != v:
        graph[u].append(v)
        graph[v].append(u)

bfs()
# print(graph)
# print(cnt[1:])
for i in cnt[1:]:
    print(i)
