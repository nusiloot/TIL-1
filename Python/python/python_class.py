class Dog:
    # MyDogList (파스칼 케이스)
    # myDogList (카멜 케이스)
    
    kind = 'canine' # 클래스 변수

    # 인스턴스를 만들기 위해서는 생성자가 필요하다.
    # self가 첫번째 인자로 꼭 필요하다
    def __init__(self, name):
        self.name = name #인스턴스 변수


my_dog = Dog('gazi')
your_dog = Dog('namu')


print(my_dog.kind)
print(your_dog.kind)

print(my_dog.name)
print(your_dog.name)

class Dog:
    # 이름에 맞게 사용하는것이 가장 바람직하다
    tricks = []   # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        

    def add_trick(self, trick):
        self.tricks.append(trick)

my_dog = Dog('gazi')
your_dog = Dog('namu')

my_dog.add_trick('hello')
your_dog.add_trick('hihi')

#클래스변수는 모든 인스턴스가 참조한다.
print(my_dog.tricks)
print(your_dog.tricks)


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = [] #인스턴스 변수가 각각 가져가고 싶으면 인스턴스 안에 넣어야 한다.

    def add_trick(self, trick):
        self.tricks.append(trick)

    

my_dog = Dog('gazi')
your_dog = Dog('namu')

my_dog.add_trick('hello')
your_dog.add_trick('hihi')

#클래스변수는 모든 인스턴스가 참조한다.
print(my_dog.tricks)
print(your_dog.tricks)

variable = 'apple'
# 단축형
print(variable.capitalize())
# self가 작성되는 이유
print(str.captiablize(variable))


# 절차 지향 vs 객체 지향
# 데이터가 흘러 다니는 것으로 보는 시간 -> 데이터가 중심이 되는 시각

# 절차 지향
# greeting(데이터)
def greeting(name):
    return f'hello,{name}'

print(greeting('harry'))

# 객체 지향
# 데이터.greeting()
class person:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        return f'hello,{self.name}' 
        # 인스턴스 자기 자신의 이름 


my_name = person('jihye')

print(my_name.greeting())
