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

# multiline="""안녕하세요.파이썬 세계로 오신걸
# 환영합니다.
# 파이썬은 비단뱀 처럼 매력적인 언어입니다."""

# a = (multiline,'\n')
# print(a,'')


# import random

# print('>>숫자 맞추기 게임<<')

# com = random.randint(1,10)

# while True :
#     my = int(input('예상 숫자를 입력하시오 : '))
#     if my == com :
#         print('~~ tjdrhd~~')
#         break
#     elif my > com :
#         print('더 작은 수를 ')

#     elif my<com :
#         print('더큰수를 생각')

# result = [1,2,3,4]
# result = result*2

# print(result)

# result.sort()

# print(result)

# result.sort(reverse = True)

# print(result)

# import random 

# r = []
# for i in [5,6,7,8] :

#     r.append(random.randint(1,5))




# lst = list(range(1,10))
# print(lst)
# t3=tuple(lst)
# print(t3)


# print(len(t3), type(t3))
# print(t3.count(3))
# print(t3.index(4))

# s = {1,3,5,3,1}

# print(len(s))
# print(s)

# for d in s :
#     print(d,end= '')

# s2 = {3, 6}

# print(s.union(s2))
# print(s.difference(s2))
# print(s.intersection(s2))

# s3 = {1, 3, 5}
# print(s3)

# s3.add(7)
# print(s3)

# s3.discard(3)
# print(s3)

# dic = dict(a = 100, b = 200 , c = 300)
# print(dic)

# person = {'닉' : '홍','살' : '35' , '주' : '서'}
# # print(person['닉'])

# print(person['살'])
# print('살' in person)

# for key in person.keys() :
#     print(key)

# for v in person.values() :
#     print(v)

# for d in person.items() :
#     print(d)

import random
charset = ['abe', 'code', 'band' ,'band', 'abc']
wc = {}
for key in charset :
    wc[key] = wc.get(key, 0 ) +1
    print(wc)

