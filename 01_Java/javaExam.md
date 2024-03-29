# Java Test

### * Java의 기초 구문

1.  자바 언어는 ***동적로딩을 지원***. ***운영체제에 독립저으로 실행할 수 있다.***
2. 자바 변수에는 ***특수언어 ('_' 제외 )가 들어갈 수 없다, 숫자로 시작할 수 없다, 명령어를 변수로 설정할 수 없다.***
3. 자바 프로그램을 실행할 시 제일 먼저 호출되는 메서드 정의는 (함수 정의)는 
   **public static void main(String args[]){}** 이다.
4. Switch 문의 식에서는 ***Float 사용할 수 없다!!!***
                                      **Char, String, Int* 는 사용가능하다.
5. 자바의 기본형 중에서 값의 저장 범위가 가장 큰 타입은 ***Doulbe***이다.
   ***Byte - Int - ( 담에 확인 꼭핳기 )***
6. 자바의 기본형 중에서 다른 타입으로 형 변환이어 떤 방법(강제,자동)으로든 불가능한 타입은
   ***Boolean (True, Flase)***이다.
7. 변수 선언 구문 작성 예시
   **int su = 1;**
   **char munji = 'j';** < - character은 문자 따움표 하나
   **String ma = "jihye";** <- String은 문자 따움표 ***두개***
   **Boolean flag= false;** 
8. ["결과: "+ 100+200 ] 의 결과는
   **결과: 100200** 으로 출력된다.
9. 연산자가 변수 ***앞에/뒤에*** 오느냐에 따라서 계산 출력 값이 다르게 표시된다.
   ex. int a= ++10;    =>   10으로 나온다. ***(출력하고 계산값 입력)***
   ex. int b= 10++;    =>   11으로 나온다. ***(출력할때 계산 입력됨)***
10. boolean type은 
    **++ / -- / + / -   같은거 안돼안돼안!!!! **
    **== / >=  / <= / instanced 된다 된다 된다 :) ** <= oky????



### Java의  OOP 구문

11. emp 라는 변수가 참조하게 된 객체가 Employee 객체인지 체크하려 할때 사용되는 연산자는 
    ***instanceof*** 이다!

12. 상속 불가한 클래스를 정의하려 할때 사용되는 제어자는
    ***final***로 표시한다. 

13. 클래스명으로 호출 가능한 메서드를 정의하려 할때 사용되는 ***제어자***

    * **static**

    클래스명으로 호출 가능한 메서드를 정의하려 할때 사용할 수 ***없는 제어자***

    * **public / final / protected**

14. 생성자 메서드에 대한 설명글 
    1)   ***메서드명이 클래스명과 동일***해야한다.
    2)   리턴값의 타입은 ***생략***한다.
    3)   ***여러 개로 오버로딩*** 가능하다.
    4)   ***생성자 메서드 구현을 생략해도*** 컴파일 오류가 발생하지 않는다.

15. 메서드 오버라이딩 규칙을 설명하는 글
    1)   오버라이딩 하려는 부모 메서드의 명칭과 동일해야 한다.
    2)   오버라이딩하려는 부모 메서드의 접근제어자는 웒하는대로 변경 불가능하다.
    3)   오버라이딩하려는 부모 메서드의 리턴값과 동일해야 한다.
    4)   오버라이딩하려는 부모 메서드의 매개변수 사양이 동일해야 한다.

16. 동일 클래스의 다른 생성자 메서드 호출시 사용되는 것은
    **this()**

17. 동일 패키지이거나 자손에서만 접근 가능한 메서드를 정의할때 사용되는 제어자는
    **private / public or 접근 제어자를 생략**

18. Abstract 클래스에 대한 설명하는 글
    1)   abstract 클래스를 상속하여 자식 클래스를 구현할 때는 implements절을 사용하여 상속X

    ​																				    		***interface***를 사용ㅎ한다.
    2)   객체 생성은 불가하며 상속만 가능하다.
    3)   abstract 메서드를 0개 이상 정의할 수 있다.
    4)   abstract클래스는 final제어자를 함께 지정할 수 없다. 

19. 객체 생성을 설명하는 글
    1)    new 뒤에 생성자 메서드를 호출하여 객체를 생성한다.
    2)    객체 생성시 조상 클래스들의 객체도 생성된다.
    3)    객체를 생성한 후에 객체의 접근 가능한 모든 멤버를 사용하려면 객체의 클래스 타입고 동일한 변수에 저장해서 사용한다.

20. 메서드 호출 시 IOException 예외가 발생한 경우 출력되지 않는 숫자를 고르면?

    ~~~ java
    try{
      System.out.println(1);
      test();
      System.out,println(2);
    }
    catch(IOException e){
      System.out.println(3);
    } 
    finally{
      System.out.println(4);
    }
    
    //정답은 2는 안나온다.
    // 1, 3, 4는 나온다!!!!!!!!!!!!!
    ~~~

    

21. 자바 소스를 작성할 때 가장 위에 작성하는 구문은?

22. "조상유형의 변수로 자손의 객체를 참조할 수 있다. 
      **조상 유형의 변수로 자손에서 추가된 멤버는 자손 유형으로 강제 형변환하여 접근"**
      는 말은 OOP언어의 어떠한 구문에 대한 설명인가?!?!

    *** Answer is 다형성***

### Java의 기본 API 활용

23. Object클래스가 포함되어 있는 패키지 명은?
    ***java.lang***

24. 어떤 객체든 전달받을 수 있는 매개변수를 선언하려고 하면
    ***Ojbect타입으로 매개변수를 선언해야 한다.***

25. Math.random() 메서드로 난수를 추출하려고 할때 어떤 식으로 
    ex. 3부터 10사이의 난수!! 

    ~~~java
    (int)(Math.random()*8+3);
    ~~~

26. 표준 입력 장치로 부터 웒하는 타입의 데이터들을 읽어오는 기능을 제공하는 클래스로서 **next(), nextInt(), nextDouble(), nextLine()**을 제공하는 것은??
    ***Answer is 'java.Scanner'***

27. '참좋하는 객체가 존재하지 않음'을 의미하는 Java언어의 리터럴은?
    **Answer is 'null'**

28. Static에 대한 설명글

    1)   main() 메서드는 반드시 static을 설명해야한다.
    2)   static 변수와 static 메서드는 클래스 로딩 과정에서 메모리가 할당되고 사용가능한 상태가 된다.
    3)   static 변수는 클래스의 객체를 생성하는 동안 메모리 영역을 할당한다.
    4)   static 변수와 static메서드는 클래스명에, 연산자를 *사용할 수 없다.*

    