-- 1. 미국에 살지 않는 고객의 풀네임, 커스터머id, 국가 보여주기

SELECT DISTINCT country FROM customers;
SELECT FirstName, LastName, CustomerId, Country FROM customers WHERE Country != 'USA';
SELECT FirstName||" "||LastName AS Fullname, CustomerId, Country FROM customers WHERE Country != 'USA';

-- 2. 브라질에 살고 있는 고객 보여주기

SELECT * FROM customers WHERE Country = "Brazil";

-- 3. 브라질 고객의 송장을 보여주는 쿼리를 제공합니다.
-- 결과 테이블에는 고객의 전체 이름, 송장 ID, 송장 날짜 및 청구 국가가 표시되어야 합니다.

SELECT C.FirstName || " " || C.LastName AS FullName, I.InvoiceId, I.InvoiceDate, I.BillingCountry
FROM customers C
LEFT JOIN invoices I -- 고객 정보를 그대로 두고 인보이스 정보를 더 넣기 위해서 LEFT JOIN 사용
ON C.CustomerId = I.CustomerId
WHERE C.Country = "Brazil";

-- 4. sales_agents.sql: Provide a query showing only the Employees who are Sales Agents.
-- 4. sales_agents.sql: 판매 대리인인 직원만 표시하는 쿼리를 제공하십시오.

SELECT * FROM employees
WHERE Title = "Sales Support Agent";

-- 5. unique_invoice_countries.sql: Provide a query showing a unique/distinct list of billing countries from the Invoice table.
-- 5. unique_invoice_countries.sql: 송장 테이블에서 청구 국가의 고유/고유 목록을 표시하는 쿼리를 제공합니다.

SELECT DISTINCT BillingCountry FROM invoices;

-- 6. sales_agent_invoices.sql: Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.
-- 6. sales_agent_invoices.sql: 각 판매 에이전트와 연결된 송장을 표시하는 쿼리를 제공합니다. 결과 테이블에는 영업 에이전트의 전체 이름이 포함되어야 합니다.

SELECT A.InvoiceId, A.CustomerId, A.InvoiceDate, employees.FirstName || " " || employees.LastName as FullName
FROM (SELECT * FROM invoices
INNER JOIN customers
ON invoices.CustomerId = customers.CustomerId) as A
INNER JOIN employees
ON A.SupportRepId = employees.EmployeeId;

-- 7. invoice_totals.sql: Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.
-- 7. invoice_totals.sql: 모든 송장 및 고객에 대한 송장 합계, 고객 이름, 국가 및 판매 대리점 이름을 표시하는 쿼리를 제공합니다.

SELECT A.Total, A.LastName || " " || A.FirstName as FullName, A.Country, employees.FirstName || " " || employees.LastName as EmpFullName
FROM (SELECT * FROM invoices
INNER JOIN customers
ON invoices.CustomerId = customers.CustomerId) as A
INNER JOIN employees
ON A.SupportRepId = employees.EmployeeId;


-- 8. total_invoices_{year}.sql: How many Invoices were there in 2009 and 2011?
-- 8. total_invoices_{year}.sql: 2009년과 2011년에 몇 개의 인보이스가 있었습니까?

SELECT COUNT(*)
FROM invoices
WHERE SUBSTR(invoices.InvoiceDate, 0, 5) = "2009"
OR SUBSTR(invoices.InvoiceDate, 0, 5) = "2011";

-- 9. total_sales_{year}.sql: What are the respective total sales for each of those years?
-- 9. total_sales_{year}.sql: 각 연도의 총 매출은 얼마입니까?

SELECT SUBSTR(invoices.InvoiceDate, 0, 5), SUM(invoices.Total)
FROM invoices
WHERE SUBSTR(invoices.InvoiceDate, 0, 5) 
BETWEEN "2009" AND "2011"
GROUP BY SUBSTR(invoices.InvoiceDate, 0, 5);

-- 10. invoice_37_line_item_count.sql: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.
-- 10. invoice_37_line_item_count.sql: InvoiceLine 테이블을 보고 Invoice ID 37에 대한 라인 항목 수를 계산하는 쿼리를 제공합니다.

SELECT COUNT(*)
FROM invoice_items
WHERE invoice_items.invoiceId = 37;

-- 11. line_items_per_invoice.sql: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: GROUP BY
-- 11. line_items_per_invoice.sql: InvoiceLine 테이블을 보고 각 Invoice에 대한 라인 항목 수를 계산하는 쿼리를 제공합니다. 힌트: 그룹화 기준

SELECT invoice_items.invoiceId, COUNT(*)
FROM invoice_items
GROUP BY invoice_items.invoiceId;

-- 12. line_item_track.sql: Provide a query that includes the purchased track name with each invoice line item.
-- 12. line_item_track.sql: 각 송장 라인 항목에 구매한 트랙 이름을 포함하는 쿼리를 제공합니다.

SELECT I.InvoiceLineId, I.TrackId
FROM invoice_items as I
ORDER BY I.InvoiceLineId;

-- 13. line_item_track_artist.sql: Provide a query that includes the purchased track name AND artist name with each invoice line item.
-- 13. line_item_track_artist.sql: 구매한 트랙 이름과 아티스트 이름을 포함하는 쿼리를 각 송장 라인 항목과 함께 제공합니다.

SELECT I.*, T.Name, A.Name
FROM invoice_items I
JOIN tracks T ON I.TrackId = T.TrackId
JOIN albums Al ON T.AlbumId = Al.AlbumId
JOIN artists A ON A.ArtistId = Al.ArtistId;

-- 14. country_invoices.sql: Provide a query that shows the # of invoices per country. HINT: GROUP BY
-- 14. country_invoices.sql: 국가별 송장 수를 표시하는 쿼리를 제공합니다. 힌트: 그룹화 기준

SELECT I.BillingCountry, COUNT(*)
FROM invoices I
GROUP BY I.BillingCountry;

-- 15. playlists_track_count.sql: Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resulant table.
-- 15. playlists_track_count.sql: 각 재생 목록의 총 트랙 수를 표시하는 쿼리를 제공합니다. 재생 목록 이름은 결과 테이블에 포함되어야 합니다.

SELECT PT.PlaylistId, P.Name, COUNT(*)
FROM playlists P
JOIN playlist_track PT ON P.PlaylistId = PT.PlaylistId
GROUP BY PT.PlaylistId;

-- 16. tracks_no_id.sql: Provide a query that shows all the Tracks, but displays no IDs. The result should include the Album name, Media type and Genre.
-- 16. Tracks_no_id.sql: 모든 트랙을 표시하지만 ID는 표시하지 않는 쿼리를 제공합니다. 결과에는 앨범 이름, 미디어 유형 및 장르가 포함되어야 합니다.

SELECT T.Name, A.Title, M.Name, G.Name
FROM tracks T
JOIN albums A ON T.AlbumId = A.AlbumId
JOIN media_types M on M.MediaTypeId = T.MediaTypeId
JOIN genres G ON G.GenreId = T.GenreId;

-- 17. invoices_line_item_count.sql: Provide a query that shows all Invoices but includes the # of invoice line items.
-- 17. invoices_line_item_count.sql: 모든 송장을 표시하지만 송장 라인 항목의 수를 포함하는 쿼리를 제공합니다.

SELECT I.*, COUNT(IT.*)
FROM invoices I
LEFT JOIN invoice_items IT ON I.InvoiceId = IT.InvoiceId;

-- 18. sales_agent_total_sales.sql: Provide a query that shows total sales made by each sales agent.
-- 18. sales_agent_total_sales.sql: 판매 대리점별 총 매출을 조회하는 쿼리를 제공한다.

SELECT I.*, COUNT(DISTINCT IT.InvoiceLineId)
FROM invoices I
JOIN invoice_items IT ON I.InvoiceId = IT.InvoiceId
GROUP BY I.InvoiceId;

-- 19. top_2009_agent.sql: Which sales agent made the most in sales in 2009?
--     Hint: Use the MAX function on a subquery. top_agent.sql: Which sales agent made the most in sales over all?
-- 19. top_2009_agent.sql: 2009년 가장 많은 매출을 올린 판매원은?
--      힌트: 하위 쿼리에서 MAX 함수를 사용하십시오. top_agent.sql: 전체 판매 실적이 가장 많은 판매 대리점은?

SELECT EmployeeName, MAX(Sales)
FROM (SELECT E.FirstName||" "||E.LastName AS EmployeeName, SUM(IT.UnitPrice * IT.Quantity) AS Sales
FROM employees E
JOIN customers C ON E.EmployeeId = C.SupportRepId
JOIN invoices I ON I.CustomerId = C.CustomerId
JOIN invoice_items IT ON IT.InvoiceId = I.InvoiceId
WHERE SUBSTR(I.InvoiceDate, 0, 5) = "2009"
GROUP BY EmployeeId);

-- 21. sales_agent_customer_count.sql: Provide a query that shows the count of customers assigned to each sales agent.
-- 21. sales_agent_customer_count.sql: 각 판매 대리점에 할당된 고객 수를 보여주는 쿼리를 제공한다.

SELECT E.FirstName||" "||E.LastName AS EmployeeName, COUNT(*)
FROM customers C
JOIN employees E ON E.EmployeeId = C.SupportRepId
GROUP BY E.EmployeeId;

-- 22. sales_per_country.sql: Provide a query that shows the total sales per country.
-- 22. sales_per_country.sql: 국가별 총 매출을 보여주는 쿼리를 제공한다.



-- 23. top_country.sql: Which country's customers spent the most?
-- 23. top_country.sql: 고객이 가장 많이 지출한 국가는 어디입니까?


-- 24. top_2013_track.sql: Provide a query that shows the most purchased track of 2013.
-- 24. top_2013_track.sql: 2013년 가장 많이 구매한 트랙을 보여주는 쿼리를 제공합니다.


-- 25. top_5_tracks.sql: Provide a query that shows the top 5 most purchased songs.
-- 25. top_5_tracks.sql: 가장 많이 구매한 상위 5곡을 보여주는 쿼리를 제공합니다.


-- 26. top_3_artists.sql: Provide a query that shows the top 3 best selling artists.
-- 26. top_3_artists.sql: 가장 많이 팔린 3명의 아티스트를 보여주는 쿼리를 제공합니다.


-- 27. top_media_type.sql: Provide a query that shows the most purchased Media Type.
-- 27. top_media_type.sql: 가장 많이 구매한 Media Type을 보여주는 쿼리를 제공한다."