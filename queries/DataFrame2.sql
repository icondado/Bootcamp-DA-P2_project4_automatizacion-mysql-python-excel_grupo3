SELECT
    f.film_id,
    LOWER(TRIM(f.title)) AS title,
    LOWER(TRIM(f.description)) AS description,
    LOWER(TRIM(c.name)) AS category,
    LOWER(TRIM(l.name)) AS language,
    COUNT(i.inventory_id) AS total_inventory,
    CASE
        WHEN f.length >= 120 THEN 1
        ELSE 0
    END AS is_long_film
FROM film f
JOIN film_category fc 
    ON f.film_id = fc.film_id
JOIN category c 
    ON fc.category_id = c.category_id
JOIN language l 
    ON f.language_id = l.language_id
LEFT JOIN inventory i 
    ON f.film_id = i.film_id
WHERE f.length > 0
  AND f.rating IS NOT NULL
GROUP BY 
    f.film_id,
    f.title,
    f.description,
    c.name,
    l.name,
    f.length;
			  
			



