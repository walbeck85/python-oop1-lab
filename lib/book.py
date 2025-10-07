# lib/book.py

class Book:
    """
    Book model for the bookstore lab.

    Attributes
    ----------
    title : str
        Required at initialization.
    page_count : int
        Required; validated via property to be an integer.
    """

    def __init__(self, title, page_count):
        # Assign via property so validation applies from the start
        self.title = title
        self.page_count = page_count

    # ---- Property: page_count (validated as int) ----
    def get_page_count(self):
        """
        Getter for page_count. We store the real value in _page_count to
        avoid accidentally calling the setter from inside the setter.
        """
        return getattr(self, "_page_count", None)

    def set_page_count(self, value):
        """
        Setter for page_count. Must be an integer. If not, print the exact
        message the lab requires so tests pass.
        """
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    # ---- Behavior: turn a page ----
    def turn_page(self):
        """
        Simulate turning a page by printing the exact string required by tests.
        """
        print("Flipping the page...wow, you read fast!")