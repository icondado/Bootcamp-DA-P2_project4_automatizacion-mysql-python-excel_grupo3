SELECT 
    f.film_id,
    f.title,
    a.actor_id,
    CONCAT(LOWER(TRIM(a.first_name)), ' ', LOWER(TRIM(a.last_name))) AS actor_full_name,
    (
        SELECT COUNT(*) 
        FROM film_actor fa2
        WHERE fa2.film_id = f.film_id
    ) AS num_actors_per_film,
    (
        SELECT COUNT(*) 
        FROM film_actor fa3
        WHERE fa3.actor_id = a.actor_id
    ) AS num_films_per_actor
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id;