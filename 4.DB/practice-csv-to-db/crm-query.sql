-- 1. 특정 사용자(한 명 이름 잡아서(UUID))가 구매한 주문 내역(order)을 모두 가져오시오.

select *
from user U
join orders O on U.uuid = O.userid
join orderitem OI on O.uuid = OI.orderid
where U.uuid = "003f6941-ae9a-4196-982f-eee62da70b88";

select *
from user U
join orders O on U.uuid = O.userid
join orderitem OI on O.uuid = OI.orderid
order by U.name, U.uuid asc;

select u.uuid, u.name, o.orderat, s.name as storename, i.name as itemname
from user u
join order o on u.uuid = o.userid
join store s on o.storeid = s.uuid
join orderitem oi on o.uuid = oi.orderid
join item i on oi.itemid = i.uuid
where u.uuid = "003f6941-ae9a-4196-982f-eee62da70b88";


-- 2. 특정 사용자(한 명 이름 잡아서(UUID))가 구매한 주문 내역의 상품명을 모두 가져오시오(유닉한 상품명).

select U.name, I.name || " " || I.type as Itemname
from user U
join orders O on U.uuid = O.userid
join orderitem OI on O.uuid = OI.orderid
join item I on OI.itemid = I.uuid
where U.uuid = "003f6941-ae9a-4196-982f-eee62da70b88";

-- 3. 특정 사용자가 구매한 매출액의 합산을 구하시오.

select name, sum(price)
from (select U.name as name, I.uuid, I.name, I.unitprice as price
from user U
join orders O on U.uuid = O.userid
join orderitem OI on O.uuid = OI.orderid
join item I on OI.itemid = I.uuid
where U.uuid = "003f6941-ae9a-4196-982f-eee62da70b88") ;

-- 4. 상점별 월간 통계(매출액)을 구하시오.

select S.uuid, S.name, substr(O.orderat, 0, 8) as months, sum(I.unitprice)
from store S
join orders O on O.storeid = S.uuid
join orderitem OI on O.uuid = OI.orderid
join item I on OI.itemid = I.uuid
where S.uuid="0c81697f-456c-4dc3-a249-9c0495ae2521"
group by substr(O.orderat, 0, 8);

-- #5 가게 별 주문액 보기 

select S.uuid, S.name, sum(I.unitprice)
from store S
join orders O on O.storeid = S.uuid
join orderitem OI on O.uuid = OI.orderid
join item I on OI.itemid = I.uuid
group by S.uuid;

-- #6 주문액이 가장 많은 가게 보기

select S.uuid as storeid, S.name as storename, sum(I.unitprice) as totalprice
from store S
join orders O on O.storeid = S.uuid
join orderitem OI on O.uuid = OI.orderid
join item I on OI.itemid = I.uuid
group by S.uuid
order by totalprice desc
limit 1;

-- #7 특정 아이템을 가장 많이 판 가게 보기

select storeid, max(totalsales)
from (select S.uuid as storeid, S.name, I.name, count(*) as totalsales
from store S
join orders O on S.uuid = O.storeid
join orderitem OI on OI.orderid = O.uuid
join item I on I.uuid = OI.itemid
where I.uuid = "5d6101d1-0653-4b50-a839-9c057dad1821"
group by storeid -- group by에 count 넣으면 연산이 적을 거 같음
order by totalsales desc);

-- #8 특정 사람이 방문한 모든 가게 보기

select U.uuid, U.name, S.uuid, S.name
from user U
join orders O on O.userid = U.uuid
join store S on S.uuid = O.storeid
where U.uuid ="003241cc-d595-4db8-bc25-43ab47080c55";

-- #9 특정 가게에서 사용자별로 구매액 확인하기

select U.uuid, U.name, S.uuid, S.name, sum(I.unitprice)
from user U
join orders O on O.userid = U.uuid
join store S on S.uuid = O.storeid
join orderitem OI on OI.orderid = O.uuid
join item I on I.uuid = OI.itemid
where S.uuid ="823865b1-0d0e-4ef2-b368-d9dfe2e49121"
group by U.uuid
order by sum(I.unitprice) desc;

-- #10 특정 가게에서 가장 돈을 많이 쓴 사용자 확인하기

select U.uuid as userid, U.name as username, sum(I.unitprice) as TotalSales
from user U
join orders O on O.userid = U.uuid
join store S on S.uuid = O.storeid
join orderitem OI on OI.orderid = O.uuid
join item I on I.uuid = OI.itemid
where S.uuid ="823865b1-0d0e-4ef2-b368-d9dfe2e49121"
group by U.uuid
order by sum(I.unitprice) desc
limit 10;

-- #11. 오늘 날짜의 주문 조회하기
