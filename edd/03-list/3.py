tex = ''
while (cmd := input()) != 'end':
  match cmd:
    case cmd if cmd.isdigit():
      tex += cmd
    case cmd if cmd.startswith('C'):
      tex = tex[:-1]
    case cmd if cmd.startswith('D'):
      _, k = cmd.split()
      k = int(k)
      if k <= len(tex):
        tex = tex[:-k]
    case cmd if cmd.startswith('M'):
      _, i, j = cmd.split()
      i, j = int(i), int(j)
      if i - 1  >= 0 and j - 1 < len(tex):
        print(tex[i-1:j])