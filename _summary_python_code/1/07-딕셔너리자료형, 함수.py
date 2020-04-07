from pprint import pprint
# 딕셔너리를 예쁘게 출력시킬수 있는 모듈이다.

dic1 = {1: '일', '이': 2, '3~5': [3, 4, 5]}
print(dic1)
"""딕셔너리(dictionary):
사전과 같이, 단어와 뜻이 짝으로 묶여있는 관계를 컴퓨터에서는 연관배열, 해시라고 하는데.
이렇게 둘이 짝으로 묶여 쓰이는 자료형을 딕셔너리(사전) 자료형이라 한다.

빈 딕셔너리는 {}로 선언하면 된다.
dict()함수로 다른 자료형을 딕셔너리 자료형으로 변환할 수 있는데, 
dict([1, '일'], [2, '이'])  나,  dict((1, '하나'), (2, '둘')) 
처럼 키와 값을 묶어준 상태의 리스트나 튜플을 딕셔너리로 변환할 수 있다.

딕셔너리의 구조는 키(key)와 값(value)이 각각 한쌍으로 묶인(key : value) 형태다. 
여러개의 쌍이 들어갈 수도 있는데, ,를 사용해서 구분해 주면 된다.
(key 에는 변하지 않는 값(immutable)이 쓰이고, value 에는 변하는 값(mutable)이나 변하지 않는 값도 쓰인다.)
그래서 리스트나 튜플처럼 인덱스(순서)로 값을 구하지 않고, 키를 사용해서 원하는 값에 접근 할 수 있다.(반대로 접근할 수도 있다.)

딕셔너리 자료형도 중첩이 가능하다.
참고로 for 변수 in 딕셔너리
같이하면, 딕셔너리의 키만 추출된다.
"""
dic2 = {1: '일'}
print("처음 상태 :", dic2)
dic2[2] = ['이', '둘']
print("추가 후 :", dic2)
del dic2[1]
print("삭제 후 :", dic2)
print("key 로 검색 걸과: ", dic2[2])
dic2[2] = '둘'
print("수정 후: ", dic2)
""" 딕셔너리 추가, 삭제, 검색, 수정:
(딕셔너리는 반복중에 크기가 바뀌면(추가, 삭제하면) 에러가 난다. 중요)
b = [1]
for a in b:
    print(b, a)
    b.append(a)
    print(b)
(반대로 리스트는 반복중에 크기를 건들여도 뭐라 안해서, 이렇게 몰래? 무한루프를 만들수 있다.)

딕셔너리 추가는  <딕셔너리이름>[<추가할 키값>] = <추가할 value 값>
과 같이 해주면 된다. 

그리고 딕셔너리 삭제는 리스트와 비슷하게  del <딕셔너리이름>[<삭제할 키값>]
과 같이 하면 키와 value 한 쌍이 없어진다.

딕셔너리 검색은 key 값을 사용해서 value 를 얻는다.  <딕셔너리이름>[<키이름>]
과 같은데, 리스트에서 []안에 인덱스를 넣은것 대신 딕셔너리에선 키값이 들어가는 것 빼곤 리스트와 동일하다.
이걸로 key 값과 매칭되는 value 를 구할 수 있고, 여기에 = 을 추가하면 value 값을 수정해줄수 있다.

주의할 점은 key 가 가리키는 값들이 여러개일 경우(중복되는 key 값이면) 하나를 제외한 나머지가 무시된다.
그리고 key 에선 변하지 않는 값이 들어가므로, 수정가능한 리스트는 key 값이 될수 없다.(대신 튜플은 수정불가여서 key 가 될 수 있다.)

그리도 어느 자료형같이 딕셔너리도 함수가 있다. 
"""
dic3 = {'도교': ['노자', '장자', '정렴'], '불교': ['석가모니', '원효', '지눌'], '유교': ['맹자', '공자', '이황', '이이']}
print()
print(dic3.keys(), list(dic3.keys()), sep='\n리스트로는: ')
'''.keys() 함수:
딕셔너리의 모든 key 를 반환한다. 
(2.7버전까진 리스트를 반환했지만, 메모리 낭비땜시 3.0부턴 dict_keys 객체로 반환한다. 근데 list 처럼 반복되는 구조라 걍 써도 된다.)
'''
print(dic3.values(), list(dic3.values()), sep='\n리스트로는: ')
'''.values() 함수:
딕셔너리의 모든 value 를 반환한다.
(얘도 .keys()처럼 자체적으로 dict_values 객체를 반환하고, 리스트로 변환해도된다.)
'''
print(dic3.items(), list(dic3.items()), sep='\n리스트로는: ')
'''.items() 함수:
딕셔너리의 key 와 value 쌍을 튜플로 묶은 상태로 반환한다.
(문답무용, 걍 얘도 dict_items 객체로 반환하고 리스트로 변환해도된다.)
'''
print(dic3.get('도교'), dic3.get('기독교'), dic3.get('기독교', '입력한 키가 읎어요'))
'''.get() 함수:
key 로 value 를 검색하는 dic3[key] 와 dic3.get(key) 둘이 서로 같은 역할이다.
차이점은 존재하지 않는 키(nokey)를 적었을 때, dic3[key]는 에러를 발생시키고, .get()은 None 을 반환한다.
한술 더떠서 .get()에 매개변수를 하나더 추가해주면, 없는 키일 경우 None을 반환하는 대신 아까 추가한 매개변수 값을 반환한다.
'''
dic3.update({'유교': ['공자', '맹자', '증자'], '기독교': ['예수', '베드로', '바울']})
print(dic3)
'''.update() 함수:
 key 와 value 쌍을 전달받아서 딕셔너리에 수정하거나 없다면 추가한다.
 키가 문자열이면, update(키=값[, 키=값,...]) 과같이 사용할 수 있고,
 update(리스트), update(튜플)도 사용가능(이때 인자값이 둘씩 묶여 있어야함.)
 그외에도 update(반복가능한객체)도 가능, 대표적인 예가 zip객체.
'''

dic3.setdefault('원불교')
print(dic3)
'''.setdefault() 함수:
인자가 하나면, 인자값 : None 형식의 쌍을 딕셔너리에 추가함. (인자를 키로 추가하고, 키에 대한 값을 None으로 저장)
인자가 둘이면, 인자1값 : 인자2값 형식의 쌍을 딕셔너리에 추가함. (인자1을 키로, 인자2를 값으로 저장)
update()함수와 비슷하지만, setdefault()는 추가만 되고 update()처럼 수정은 불가능.
'''

dic3.pop('원불교')
print(dic3, dic3.pop('수어지교', '얘는 없는 키'))
'''.pop() 함수:
key 로 value 와 함께 삭제하는 del dic3[key] 과 dic.pop(key) 둘이 서로 같은 역할이다.
차이점은 pop()함수는 값을 반환한다.
존재하지 않는 키(nokey)를 인자값으로 넘기면, None을 반환하는 .get()과 다르게 keyerror를 반환한다.
인자값을 하나더 추가하면, 없는 키일 경우 None을 반환하는 대신 두번째 인자값을 반환한다.
'''

dic3.popitem()
print(dic3)
'''.popitem() 함수:
파이썬 3.5이전에서는 임의의 키, 값 묶음을 삭제하고 튜플로 반환하지만,
파이썬 3.6이후에서는 딕셔너리의 마지막 키, 값 묶음을 삭제하고 튜플로 반환한다.
'''

dic4 = dic3.copy()
print(dic4)
dic4.clear()
print(dic4)
'''.clear(), .copy() 함수:
다른자료형처럼 딕셔너리 자료형에서도 사용가능 하며, 방법은 동일하게
빈상태로 초기화, 복사다.
'''

print(dic3.fromkeys([1, 2, 3, 4]))
print(dic3.fromkeys((1, 2, 3, 4), '값'))
print(dic3.fromkeys([1, 2, 3, 4], (10, 20, 30, 40)))
'''.fromkeys() 함수:
리스트, 튜플을 인자값으로 받아, 각각의 요소들을 딕셔너리의 키로, 값은 None으로 하는 새로운 딕셔너리를 할당한다.
(기존에 있던 딕셔너리를 무시하고 새로 할당한다.)
그리고 그러한 값을 기존 딕셔너리에 적용하는 것이 아니라, 반환한다. (기존 딕셔너리의 형태는 그대로)
.setdefault()함수와 비슷한데, fromkeys()함수도 인자를 추가한다면, 그값을 모든키에 대한 값으로 지정할 수 있다.
'''

print("pprint로 출력하기 :")
pprint(dic3)
"""
추가로, in 을 사용해서 리스트의 값들과 비교했듯이, 딕셔너리에서는 키 값들과 비교해줄 수 있다. 
그래서 key 값의 존재유무에 따라 True, False 를 반환한다.
그리고 위 코드처럼 pprint() 를 사용한다면,(모듈 사용) 딕셔너리를 쌍마다 줄바꿈 해서 보기좋게 출력해줄 수 있다.
"""

