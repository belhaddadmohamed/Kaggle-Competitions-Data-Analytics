-- select director, avg(revenue) as avg_revenue
-- from tmdb_movies
-- group by director
-- order by avg_revenue desc
-- limit 10


-- select original_title, revenue, budget, `cast`
-- from tmdb_movies
-- where original_title='The Avengers'


-- select concat(substring(original_title, 0, 20), '...'), budget, revenue, genres
-- from tmdb_movies
-- where original_title='The Sound of Music' or
--       original_title='Doctor Zhivago' or
--       original_title='The Greatest Story Ever Told' or
--       original_title='Thunderball' or
--       original_title='Those Magnificent Men in Their Flying Machines or How I Flew from London to Paris in 25 hours 11 minutes';


-- select original_title, revenue, budget
-- from tmdb_movies
-- where original_title='The Karate Kid, Part II';


select original_title, revenue, budget, revenue-budget profit, concat((revenue-budget)/budget, '%') as roi
from tmdb_movies
where original_title='Jurassic Park' or
      original_title='Minions'