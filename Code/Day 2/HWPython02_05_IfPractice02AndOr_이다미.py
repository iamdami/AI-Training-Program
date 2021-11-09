userId="orange"
userPwd='1234'
vid=input("ID를 입력하세요:")
vpwd=input("pwd를 입력하세요:")
if vid == userId and vpwd == userPwd:
  print(userId + "님 로그인 성공")
elif vid != userId:
  print("ID 확인 하세요")
else :
  print("Pwd 확인 하세요")