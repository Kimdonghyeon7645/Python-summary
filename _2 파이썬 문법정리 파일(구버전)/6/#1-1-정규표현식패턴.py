# 컴퓨터과학의 농담중에 문제 하나를 정규표현식으로 풀게되면 문제가 2개가 된다. 라는 말이있다.
gusik = """ 
정규표현식(regular expression) :
정규표현식은 일정한 규칙을 가진 문자열을 표현하는 방법으로, 그러한 문자열을 식별할 때 사용함.
문자열 규칙의 집합이 복잡해지면, 외계어?가 되며, 문자열을 다룰때 매우 유용하지만 읽고 해석하기에는 매우 난해하긴함.

하지만 정규표현식도 여러개로 나열한 규칙들의 모임이라, 하나하나 쪼개보면 어렵지 않음.
"""

# 정규 표현식 > 문자열 판단
"""
^ : 이 기호 뒤에 오는 문자, 문자열, 하위표현식이 문자열의 맨 앞에 오는 패턴.
    (특정 ~으로 시작하는 문자열 인가?)

$ : 이 기호 앞에 오는 문자, 문자열, 하위표현식이 문자열의 맨 뒤에 오는 패턴.
    (특정 ~으로 끝나는 문자열 인가?)
    (정규표현식 마지막에 주로 사용, 이 기호를 쓰지 않은 것은 .* 과 동일)
    
| : 이 기호 양 옆에 오는 문자, 문자열, 하위표현식 중에서 양 옆에서 하나라도 포함되는 패턴.
    (or 연산자, ~ 또는 ~ 가 들어가는 문자열 인가?)
    (| 여러개를 같이 사용할 수 있다. ex> a|b|c|d 이럴때는 네 개중 한 개라도 문자열에 포함되는지 판단)
"""

# 정규표현식 > 범위, 특수문자
"""
0-9 : 모든 숫자(0~9) 
a-z : 모든 영문 소문자(a~z)
A-Z : 모든 영문 대문자(A~Z)

\d : 모든 숫자 (== [0~9])
\D : 숫자를 제외한 모든 문자 ( == [^0~9])
\w : 영문 대소문자, 숫자, 밑줄문자 ( == [a-zA-Z0-9_])
\W : 영문 대소문자, 숫자, 밑줄문자를 제외한 모든 문자 ( == [^a-zA-Z0-9_])
\s : 모든 화이트 스페이스 ( == [ \t\n\r\f\v])(차례대로, 공백, 탭키, 개행, 캐리지리턴, 폼피드, 수직탭)
\S : 공백( )을 제외한 모든 화이트 스페이스 ( == [^ \t\n\r\f\v])
"""

# 정규 표현식 > 범위 판단
"""
[] : 이 기호(대괄호) 안에 문자, 범위가 들어가며, 대괄호 안에 있는 문자중 하나라도 포함되는 패턴.
     
* : 이 기호 앞에 오는 문자, 문자열, 하위표현식, 대괄호로 묶은 문자들이 0개 이상 있는 패턴.
    (0개 이상이여서 대상이 문자열에 없어도 패턴을 만족)
    
+ : 이 기호 앞에 오는 문자, 문자열, 하위표현식, 대괄호로 묶은 문자들이 1개 이상 있는 패턴.
    (* 과 비슷하지만, +는 1개 이상이라 대상이 있어야만 패턴을 만족)
     
? : 이 기호 앞에 오는 문자, 문자열, 하위표현식, 대괄호로 묶은 문자들이 0개 또는 1개 있는 패턴.
    (이 기호 앞에오는 대상은 1개 아니면 없어야 패턴을 만족)

. : 아무 문자가(글자, 숫자, 기호, 공백) 1개만 있는 패턴.
    (이 기호는 정말 아무 문자 1개를 의미 하기에, 공백 1칸도 패턴을 만족)
    (\n, 개행문자를 제외한 모든 문자를 의미)
    
?! : 이 기호 뒤에 오는 문자, 문자열, 하위표현식이 해당 위치에 포함되지 않는(0개만 있는) 패턴.
     (이 기호를 쓴 해당 위치에서만 해당, 배제했던 대상이 다른 위치에서 포함해도 패턴을 만족)
     (문자열 전체에서 배제할려면 ^과 $를 앞뒤에 붙임)
    
{개수} : 이 기호 앞에 오는 문자, 문자열, 하위표현식, 대괄호로 묶은 문자들이 {}안의 개수 만큼 있는 패턴.
        ( 대상{n} : 대상이 n개 있는가?)
{ 시작개수, 끝개수 } : 대상이 시작개수 이상 끝 개수 이하의 개수만큼(시작개수~끝개수) 있는 패턴.        
     
[^ ] : 이 기호(대괄호) 안에 문자, 범위가 들어가며, 대괄호 안에 있는 문자들을 포함하지 않는 패턴.  
      (일반 [] 대괄호에 not(논리부정)연산자를 결합)
      (^[] 와 [^ ]은 서로 다른 패턴임, 유의)
"""

# 정규표현식 > 그룹
"""
() : 이 기호 안에 오는 것들은 그룹(=하위표현식) 으로 묶는 패턴.
     (정규 표현식에서 하위 표현식이 가장 먼저 우선순위를 가짐, 괄호 연산같이)
"""