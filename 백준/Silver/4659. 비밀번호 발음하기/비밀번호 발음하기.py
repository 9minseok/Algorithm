# 모음(a, e, i, o, u)는 반드시 하나 포함
# 모음 3개, 자음 3개 연속 X
# 같은 글자 연속 X, but ee와 oo는 가능

vowels = ['a', 'e', 'i', 'o', 'u']
excep = ['ee', 'oo']

while True:
  x = y = 0
  password = input()
  
  # end를 만나면 멈춰
  if password == 'end':
    break

  # 카운트 만들기
  cnt = 0

  # 모음 개수 세기
  for i in vowels:
    if i in password:
      cnt += 1
  
  # 모음 없으면 acceptable
  if cnt < 1:
    print(f'<{password}> is not acceptable.')
    continue

  # 모음, 자음 3개 연속
  for i in range(len(password) - 2):
    if password[i] in vowels and password[i+1] in vowels and password[i+2] in vowels:
      x = 1
    elif not(password[i] in vowels) and not(password[i+1] in vowels) and not(password[i+2] in vowels):
      x = 1
  
  if x == 1:
    print(f'<{password}> is not acceptable.')
    continue

  # 같은 글 체크, but ee와 oo는 가능
  for i in range(len(password) - 1):
    if password[i] == password[i+1]:
      if password[i] == 'e' or password[i] == 'o':
        continue
      else:
        y = 1
  
  if y == 1:
    print(f'<{password}> is not acceptable.')
    continue

  # 모든 케이스를 통과하면
  print(f'<{password}> is acceptable.')  