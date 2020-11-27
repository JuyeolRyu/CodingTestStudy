def dfs(current_node):
  row, col = current_node
  d_row = [-1,1,0,0]
  d_col = [0,0,-1,1]

  if visited[row][col] < 0:
    visited[row][col] = 0
    #4방향 모두 확인
    for i in range(4):
      n_row, n_col = row + d_row[i], col + d_col[i]
      print(d_row)
      print(d_col)
      print(graph)
      if 0<= n_row < n and 0<= n_col <n and graph[row][col] < graph[d_row][d_col]:
        visited[row][col] = max(visited[row][col], dfs([n_row,n_col]))
    
    visited[n_row][n_col] += 1
  return visited[n_row][n_col]
##########################################################################################

graph = []
ans = 0
n = int(input())
for i in range(n):
  graph.append(list(map(int,input().split())))
visited = [[-1] * n for _ in range(n)]

#시작점이 어디인지 모르니까 모든 지점에서 전부 시작해봄 
for row in range(len(graph)):
  for col in range(len(graph[0])):
    ans = max(ans, dfs( [row, col] ) )

print(ans)