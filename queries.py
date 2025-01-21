class Queries:
    """Class containing SQL queries for searching and recording search data."""

    def search_movies_by_keyword(self) -> str:
        """SQL query to search movies by keyword."""
        return """
        SELECT f.title, f.description
        FROM film f
        WHERE f.title LIKE %s
        LIMIT 10;
        """

    def search_by_genre_and_year(self) -> str:
        """SQL query to search movies by genre and year."""
        return """
        SELECT f.title, f.description
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        WHERE c.name = %s AND f.release_year = %s
        LIMIT 10;
        """

    def get_popular_queries(self) -> str:
        """SQL query to fetch the most popular search queries."""
        return """
        SELECT keyword, COUNT(*) AS count
        FROM keyword_queries
        GROUP BY keyword
        ORDER BY count DESC
        LIMIT 10;
        """

    def record_search_query(self) -> str:
        """SQL query to record search queries."""
        return """
        INSERT INTO keyword_queries (keyword, query_text, created_at)
        VALUES (%s, %s, NOW())
        ON DUPLICATE KEY UPDATE 
        search_count = search_count + 1;
        """
