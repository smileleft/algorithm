# 표 편집
def solution(n, k, cmds):

  deleted = []
  up = [i - 1 for i in range(n + 2)]
  down = [i + 1 for i in range(n + 1)]

  # current index
  k += 1

  # 주어진 명령어(cmd) 리스트를 하나씩 처리
  for cmd in cmds:
    if cmd.startswith("C"):
      # delete
      deleted.append(k)
      up[down[k]] = up[k]
      k = up[k] if n < down[k] else k = down[k]

    elif cmd.startswith("Z"):
      # restore most recently deleted row
      restore = deleted.pop()
      down[up[restore]] = restore
      up[down[restore]] = restore

    else:
      # move current postion with U or D
      action, num = cmd.split()
      if action == "U":
        for _ in range(int(num)):
          k = up[k]
      else:
        for _ in range(int(num)):
          k = down[k]

  # return answer
  answer = ["O"] * n
  for i in deleted:
    answer[i - 1] = "X"

  return "".join(answer)
      
