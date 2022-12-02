--AVG
select Avg(count) as "Ortalama Fiyat Tutarları" from payments



--Sum
Select SUM(count) as "Toplam Ödeme Tutarı" from payments
select sum(follower_count) as "Toplam Takipçi" from sellers


--Max
Select MAX(quantity) as "En pahalı sipariş" from orders


select Max(rating) as "Maksimum Takipçi" from sellers


--Min
Select MIN(quantity) as "En ucuz sipariş" from orders


-- COUNT 
Select COUNT(id) as "Sipariş Sayısı" from orders






--Distinct
Select DISTINCT(customer_id) from orders


--Group By
select * from payments
select type as "Ödeme Yöntemi",count(*) as "Adet" from payments
group by type



select c.name as "Kategori İsmi" ,count(*)from Products as p
inner join categories as c on p.category_id = c.id
group by c.name 


select p.stock as "Stok" ,count(*) as "Adet" from products as p 
inner join categories as c
on p.category_id = c.id
group by p.stock


select name as "Adres Tipi" , Count(*) as "Adet" from addresses 
group by name


select type as "Marka İçeriği" , count(*) as "Adet" from brands
group by type



--Having
select c.name as "Kategori İsmi" ,count(*) as "Adet" from Products as p
inner join categories as c on p.category_id = c.id
group by c.name 
having count(*)>=3


select type as "Ürün Kategorisi" , count(*) as "Adet" from brands
group by type
having type='giyim'



select co.name as "Ülke" , count(*) from countries as co 
inner join cities as ci
on co.id=ci.country_id
inner join street as s
on ci.id=s.city_id
group by co.name
having co.name ='Türkiye'





