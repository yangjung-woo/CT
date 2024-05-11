# 해시테이블 구현 방법 > 파이썬의 경우 딕셔너리로 구현되어있음 
# 1. Array list 사용 > 탐색시 소요 시간 O(1)
# 충돌시 Open addressing 방식으로 해결
 
# dict[key] = value 
d ={}

d[0] = '양정우'
d[1] = '김정우'
d[7720] = '애앵정우' # directed-address Table : key값 그대로 인덱스로 사용, 단점: 자료공간 낭비 

print(d)

# 원래 이론상 해시테이블 

def Hashfunction(key):
    return key%8

hash_d ={}

hash_d[Hashfunction(1)]= '양정우'
hash_d[Hashfunction(3)]= '정우'
hash_d[Hashfunction(5)]= '양우'
hash_d[Hashfunction(7)]= '양정'

hash_d[Hashfunction(9)]= '우' # collision 발생 
hash_d[Hashfunction(11)]= '정'
hash_d[Hashfunction(13)]= '양'
print(hash_d)

# 딕셔너리 주요 연산 

score = {'A':90,'B':70,'C':65}

if 'A' in score:  # in 함수 동작은 O(1) 매우빠른 탐색방식이다 
    print('Yes')
else:
    print('No')
