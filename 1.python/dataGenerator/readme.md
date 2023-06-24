# 데이터 생성기

* 언어 : Python

* 추후 CRM (고객관리 솔루션) 프로젝트 개발에 사용할 데이터를 생성한다

* 생성할 수 있는 데이터 : User, Store, Item, Order, Orderlist

<br/>

## 관전 포인트

* 재사용성이 높은 코드로 구성하기 위해 객체와 메소드를 최대한 이용함

* 추상클래스를 이용해 각 요소 Generator의 형식을 정의함

* 데이터 클래스를 생성한 이후에는 main.py의 selectModel 변수에 등록해주기만 하면, generateMultipleData 함수로 해당 데이터 생성 가능

* 명령줄에서 인자를 주어 데이터를 생성할 수 있도록 함<br/>
```python main.py user 10 csv```