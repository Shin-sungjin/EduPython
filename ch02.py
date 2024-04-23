#표준 입력력
# score = input() #외부로부터 입력받는 함수
# print(type(score)) #input으로 받는 결과는 문자열
# print(score)

# score = input("점수 : ")
# print(int(score)+10)

#기본적인 print 사용법
# print("I can't' Swim")
# print('\"파이썬" 언어')
# print("c:\\temp\\myfile.py") #window
# print("c:\\temp\\myfile.py") #linux
#
#
# #연결 여내산
# print("Hello"+ "Python") #문자열 연결 concat
# print("Hello" , "Python") # ,는 하나의 공백 역할을 수행
# print("Hello" "Python")


# print("Hello", 3) # str + int
# # print("Hello" 3)
# # print("Hello"+ 3)
# print("Hello" * 3) # str 뒤 곱 연산은 반복 출력

# formatting
name = "신성진"
age = 22
score = 99.9
print("이름: %s 나이:%d 점수:%.2f"%(name, age, score))
print(type(age))
print(type(score))

#자릿 수 지정
print("[%10s]"%name)  #오른쪽 정력 defalt
print("[%-10s]"%name)  #왼쪽 정렬 음수

print("[%f]"%score)     # .1f 소수점 1 자리
print("[%.1f]"%score)   #.3f 소수점 3자리
print("[%.3f]"%score)   #8.1f 전체 8자리 소수점 아래 포함
print("[%8.1f]"%score)
print("[%8.3f]"%score)
print("[%-8.1f]"%score)
print("[%-8.3f]"%score)

