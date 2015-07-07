# IPython log file

a=5
a
from numpy.random import randn
data = {i:randn() for i in range(10)}
# 0부터 range()의 parameter까지 i를 반복
# i:randn() 표준편차가 1이고 평균 값이 0인 정규분포에서 표본을 추출한다. 
data
an_apple = 27
an_example = 42
an_apple
b = [1,2,3]
b.reverse()
b
import datetime
../IPython_practice/Chapter03.ipynb
path = '../IPython_practice/Chapter03.ipynb'
path
get_ipython().magic(u'pinfo b')
#변수 이름 앞이나 뒤에 ? 기호를 붙이면 객체에 대한 일반 정보를 출력(이 기능을 객체의 자기관찰(Introspection)이라고 함)
def add_numbers(a,b):
    """
    Add two numbers together
    
    Returns
    --------
    the_sum : type of arguments
    """
    return a+b
get_ipython().magic(u'pinfo add_numbers')
get_ipython().magic(u'pinfo2 add_numbers')
#?기호를 2개 쓰면 함수의 소스코드를 보여줌
import numpy as np
get_ipython().magic(u'psearch np.*load*')
# *기호로 둘러싸인 문자열과 포함하는 모든 이름을 보여준다.
def f(x,y,z):
    return (x+y)/z
a=5
b=6
c=7.5
result=f(a,b,c)
result
get_ipython().magic(u'run test.ipynb')
#test.ipynb가 있다고 가정
2**27
#2^27
_
__
_45
#IPython은 입,출력을 포함한 전체 콘솔 세션의 로그를 %logstart를 사용하여 기록할 수 있다.
get_ipython().magic(u'logstart')
#logstop으로 중단
#IPython 로깅은 아무 때나 활성화시킬 수 있으며 과거 명령을 포함한 전체 세션을 기록
get_ipython().magic(u'logstop')
