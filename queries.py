"""
Module containing SQL queries for searching and recording search data.
"""

# SQL query to search movies by keyword
search_movies_by_keyword = """
SELECT f.title, f.description
FROM film f
WHERE f.title LIKE %s
LIMIT 10;
"""

# SQL query to search movies by genre and year
search_by_genre_and_year = """
SELECT f.title, f.description
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = %s AND f.release_year = %s
LIMIT 10;
"""

# SQL query to fetch the most popular search queries
get_popular_queries = """
SELECT keyword, COUNT(*) AS count
FROM keyword_queries
GROUP BY keyword
ORDER BY count DESC
LIMIT 10;
"""

# SQL query to record search queries
record_search_query = """
INSERT INTO keyword_queries (keyword, query_text, created_at)
VALUES (%s, %s, NOW())
ON DUPLICATE KEY UPDATE 
search_count = search_count + 1;
"""
