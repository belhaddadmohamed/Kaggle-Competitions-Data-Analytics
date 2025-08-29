-- select count(*) 
-- from Salaries;

-- SELECT JobTitle, totalpay, dense_rank() over(order by totalpay desc) as JobTitleCount
-- FROM Salaries;

-- select JobTitle, round(avg(totalpay) over(partition by lower(JobTitle)), 2) as AvgPay
-- from Salaries
-- order by AvgPay desc;

-- select upper(JobTitle) as JobTitle, count(*)
-- from Salaries
-- group by upper(JobTitle)
-- order by 2 desc;

-- select JobTitle, Year, max(totalpay) TopPaid
-- from Salaries
-- group by year
-- order by year desc;

-- select EmployeeName, TotalPay, dense_rank() over(order by TotalPay desc) Rank
-- from Salaries
-- order by TotalPay desc;

-- with ranking_CTE as (
--   select Id, EmployeeName, TotalPay, dense_rank() over(order by TotalPay desc) Rank
--   from Salaries
--   order by TotalPay desc
-- )
-- select * 
-- from ranking_CTE r1
-- join ranking_CTE r2
--   on r1.rank = r2.rank and r1.Id != r2.Id
-- order by r1.Id

select JobTitle, count(distinct EmployeeName) UniqueEmp, Year
from Salaries
where Year=2013
group by JobTitle
having UniqueEmp = 1
order by EmployeeName desc
