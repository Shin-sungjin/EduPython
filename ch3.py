"""
format 메소드
"""
name = "신성진"
age = 22
score = 99.9
print("이름:{}, 나이:{}, 점수:{}".format(name, age, score))
print("이름:{}, 나이:{}, 점수:{}".format(score, age, name))  # 순서의 영향을 받음
print("이름:{2}, 나이:{1}, 점수:{0}".format(score, age, name))  # 순서의 영향을 받음

"""
정렬 방식 
{:>10} : 전체  10 칸 차지 공백을 왼쪽에 삽입 
{:<10} : 공백 오른쪽 삽입
{:^10}  : 가운데 정렬
{:.5f} 소수점 포맷
{:,}  : 세 자리 콤마
"""
print("[{:>10}]".format(name))
print("[{:<10}]".format(name))
print("[{:^10}]".format(name))
print("[{:.10f}]".format(score))
print("[{:,}]".format(12312312312312312))
# 포멧으로 출력된 내용들은 문자열 취급

# >기호 앞에 문자열 사용하면, 공백은 문자열로 대체
print("[{:*>10}]".format(name))
print("[{:#<10}]".format(name))
print("[{:?^10}]".format(name))

#분리 사용
"""오 이런게 돼? 자바에서도 가능한가?"""
temp = "이름:{}, 나이:{}, 점수:{}"
temp = temp.format(name, age, score)
print(temp)

#f문자열
print(f"이름:{name},나이:{age}, 점수 : {score}")
print(f"이름:{name:>10},나이:{age :>10}, 점수 : {score}")
print(f"이름:{name:<10},나이:{age:<10}, 점수 : {score}")
print(f"이름:{name:^10},나이:{age:^10}, 점수 : {score}")

#포맷팅을 활용하여 url 작성하기
site = "https://api.thingspeak.com/update?api_key="
apikey ="YTRUTFY045MOB37"
v1=5
v2=10
url=f"{site}{apikey}&field={v1}&field2={v2}"
print(url)