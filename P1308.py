target = ' ' + input().lower() + ' '
graph = ' ' + input().lower() + ' '
if graph.find(target) != -1:
    print(graph.count(target) + graph.count(target.rstrip() + target), graph.find(target))
else:
    print(-1)
