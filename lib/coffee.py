# lib/coffee.py

class Coffee:
    """
    Coffee model for the bookstore lab.

    Required init args:
      - size (str): must be one of "Small", "Medium", or "Large"
      - price (int|float): current price; tip() increases by exactly 1

    Behavior:
      - tip(): prints required message and increments price by 1
    """

    _VALID_SIZES = {"Small", "Medium", "Large"}

    def __init__(self, size, price):
        """
        Initialize a Coffee. We assign via the property so that validation
        runs immediately at construction time.
        """
        self.size = size
        self.price = price

    # ---- Property: size (validated) ----
    def get_size(self):
        """
        Getter returns the private backing field. Using _size avoids
        accidentally recursing into the setter when we read.
        """
        return getattr(self, "_size", None)

    def set_size(self, value):
        """
        Setter enforces allowed sizes. If invalid, print the exact string
        required by the lab so tests pass.
        """
        if value in self._VALID_SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    size = property(get_size, set_size)

    # ---- Behavior: tip ----
    def tip(self):
        """
        Print the required message and increment price by exactly 1.
        Assumes price is numeric per lab expectations.
        """
        print("This coffee is great, here’s a tip!")
        self.price += 1