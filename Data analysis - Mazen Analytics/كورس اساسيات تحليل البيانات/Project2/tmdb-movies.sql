-- select director, avg(revenue) as avg_revenue
-- from tmdb_movies
-- group by director
-- order by avg_revenue desc
-- limit 10


select original_title, revenue, budget, `cast`
from tmdb_movies
where original_title='The Avengers'