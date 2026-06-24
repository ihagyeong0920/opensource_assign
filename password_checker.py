password = input("비밀번호를 입력하세요: ")

score = 0

if len(password) >= 8:
  score += 1
else:
  print("8자 이상 입력하세요.")

if any(c.isupper() for c in password):
  score += 1
else:
  print("대문자가 포함되어 있지 않습니다.")
  
if any(c.isdigit() for c in password):
  score += 1
else:
  print("숫자가 포함되어 있지 않습니다.")

if score == 4:
  print("비밀번호 강도 : 강함")
elif socre >= 2:
  print("비밀번호 강도 : 보통")
else:
  print("비밀번호 강도 : 약함")
