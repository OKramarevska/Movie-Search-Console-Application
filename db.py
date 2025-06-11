import os

import pymysql
from dotenv import load_dotenv

load_dotenv()


class DBConnection:
    """Database connection handler class."""

    def __init__(self) -> None:
        """Initialize database connection settings."""
        self.dbconfig: dict = {
            "host": os.getenv('DB_HOST'),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME")
        }
        self.connection = None
        self.cursor = None

    def connect(self) -> None:
        """Connect to the database and create a cursor."""
        try:
            self.connection = pymysql.connect(**self.dbconfig, charset='utf8mb4')
            self.cursor = self.connection.cursor()
            #print("Connection successful!")
        except pymysql.MySQLError as e:
            print(f"Database error: {e}")

    def close(self) -> None:
        """Close the cursor and connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
           # print("Connection closed.")

    def execute_query(self, query: str, params: tuple = None) -> None:
        """Execute a query."""
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self) -> list:
        """Fetch all results from the last executed query."""
        return self.cursor.fetchall()

    def fetch_genres(self) -> list[str]:
        """Fetch all genres from the database."""
        query = "SELECT name FROM category;"
        self.execute_query(query)
        return [row[0] for row in self.fetchall()]

    def fetch_years_for_genre(self, genre: str) -> list[str]:
        """
        Fetch available years for a given genre.

        Args:
            genre (str): The genre name.

        Returns:
            list[str]: List of years.
        """
        query = """
        SELECT DISTINCT f.release_year
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        WHERE c.name = %s;
        """
        self.execute_query(query, (genre,))
        return [str(row[0]) for row in self.fetchall()]

    def record_query(self, keyword: str, query_text: str) -> None:
        """
        Records the search query into the keyword_queries table.

        Args:
            keyword (str): The keyword or search text entered by the user.
            query_text (str): The type of query (e.g., 'keyword', 'genre_year').
        """
        query = """
        INSERT INTO keyword_queries (keyword, query_text, created_at)
        VALUES (%s, %s, NOW())
        ON DUPLICATE KEY UPDATE 
        search_count = search_count + 1;
        """
        self.execute_query(query, (keyword, query_text))
