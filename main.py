import db
import queries
import ui


class MovieSearchAppOK:
    """Movie search application class."""

    def __init__(self) -> None:
        """Initialize the application components."""
        self.db: db.DBConnection = db.DBConnection()
        self.ui: ui.UI = ui.UI()
        self.queries: queries.Queries = queries.Queries()

    def start(self) -> None:
        """Start the application."""
        self.db.connect()
        while True:
            self.ui.show_menu()
            choice: str = self.ui.get_user_choice()

            if choice == "1":
                self.search_movies_by_keyword()
            elif choice == "2":
                self.search_movies_by_genre_and_year()
            elif choice == "3":
                self.view_popular_queries()
            elif choice == "4":
                print("See you soon!")
                break
            else:
                print("Invalid choice. Try again.")


        self.db.close()

    def search_movies_by_keyword(self) -> None:
        """Search for movies by a keyword."""
        keyword: str = self.ui.get_search_keyword()
        query: str = self.queries.search_movies_by_keyword()
        self.db.execute_query(query, ('%' + keyword + '%',))
        movies: list[tuple[str, str]] = self.db.fetchall()
        self.db.record_query(keyword, "keyword")

        if not movies:
            print("Not found. Please make another try.")
        else:
            self.ui.display_movies(movies)

    def search_movies_by_genre_and_year(self) -> None:
        """Search for movies by genre and year."""
        genres: list[str] = self.db.fetch_genres()
        genre: str = self.ui.get_genre_choice(genres)

        years: list[str] = self.db.fetch_years_for_genre(genre)
        year: str = self.ui.get_year_choice(years)

        query: str = self.queries.search_by_genre_and_year()
        self.db.execute_query(query, (genre, year))
        movies: list[tuple[str, str]] = self.db.fetchall()
        self.ui.display_movies(movies)
        self.db.record_query(f"{genre} {year}", "genre_year")

    def view_popular_queries(self) -> None:
        """View the most popular search queries."""
        query: str = self.queries.get_popular_queries()
        self.db.execute_query(query)
        popular_queries: list[tuple[str, int]] = self.db.fetchall()
        self.ui.display_popular_queries(popular_queries)


if __name__ == "__main__":
    app = MovieSearchAppOK()
    app.start()
