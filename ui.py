class UI:
    """User Interface class for displaying menus and interacting with the user."""

    def __init__(self):
        """Initialize the menu items."""
        self.menu_items = [
            "Welcome to Movie World! Enjoy your search!",
            "1. Search movies by keyword",
            "2. Search movies by genre and year",
            "3. View popular search queries",
            "4. Exit"
        ]

    def show_menu(self) -> None:
        """Display the main menu to the user."""
        print(*self.menu_items, sep="\n")

    def get_user_choice(self) -> str:
        """Get the user's choice from the menu."""
        return input("Enter your choice: ")

    def get_search_keyword(self) -> str:
        """Ask the user to enter a search keyword."""
        return input("Enter search keyword: ")

    def get_genre_choice(self, genres: list[str]) -> str:
        """
        Display a list of genres and ask the user to select one.

        Args:
            genres (list[str]): List of available genres.

        Returns:
            str: Selected genre.
        """
        print("Available genres:")
        for idx, genre in enumerate(genres, 1):
            print(f"{idx}. {genre}")
        choice: int = int(input("Choose a genre by number: ")) - 1
        return genres[choice]

    def get_year_choice(self, years: list[str]) -> str:
        """
        Display a list of years and prompt the user to select one.

        Args:
            years (list[str]): List of available years.

        Returns:
            str: Selected year.
        """
        print("Available years:")
        for idx, year in enumerate(years, 1):
            print(f"{idx}. {year}")
        choice: int = int(input("Choose a year by number: ")) - 1
        return years[choice]

    def display_movies(self, movies: list[tuple[str, str]]) -> None:
        """
        Display a list of movies to the user.

        Args:
            movies (list[tuple[str, str]]): List of movies as (title, description).
        """
        if movies:
            for title, description in movies:
                print(f"Title: {title}\nDescription: {description}\n")
        else:
            print("No results found.")

    def display_popular_queries(self, popular_queries: list[tuple[str, int]]) -> None:
        """
        Display the most popular search queries to the user.

        Args:
            popular_queries (list[tuple[str, int]]): List of popular queries and their counts.
        """
        if popular_queries:
            for query, count in popular_queries:
                print(f"{query} - {count} times")
        else:
            print("No popular queries found.")
