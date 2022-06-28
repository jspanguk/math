# a = int(input('짐의 무게는 얼마입니까?'))

# if a < 10 :
#     print('수수료는 없습니다.')

# else :
#     print('수수료는 '+ format(10000,'3,d') + '원 입니다')

# a = int(input("짐의 무게는 얼마입니까?"))

# price = (a//10)*10000

# if price == 0 :
#     print('수수료는 없습니다')

# else :
#     print('수수료는 ' + format(price) + '원입니다.')

# import random

# print('>>숫자 맞추기 게임<<')
# com = random.randint(1,10)

# while True :
#     my = int(input('예상 숫자를 입력하시오 : '))

#     if my > com :
#         print('더 작은 수 입력')
    
#     elif my< com :
#         print('더 큰 수 입력')

#     else :
#         print('~~ 성공 ~~')
#         break

multiline="""안녕하세요.파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

a = (multiline,'\n')
print(a,'')


    