from decorators import timer
from time import sleep


class Gift:
    SIZES = {
        "small": {"weight": 1, "time": 1},
        "medium": {"weight": 2, "time": 3},
        "large": {"weight": 5, "time": 10}
    }
    def __init__(self, size: str):
        """
        Create a gift.

        Parameters
        ----------
        size : str
            Size of the gift. Must be one of "small", "medium" or "large".

        """
        if self.SIZES.get(size) is None:
            raise ValueError("Invalid size")
        self.size = size

    @timer
    def compute_weight(self) -> int:
        """
        Compute the weight of the gift.

        Returns
        -------
        int
            Weight of the gift.
        """
        return self.SIZES[self.size]["weight"]

    @timer
    def compute_time(self) -> int:
        """
        Compute the time to wrap the gift.

        Returns
        -------
        int
            Time to wrap the gift.

        """
        return self.SIZES[self.size]["time"]

    def wrap_gift(self):
        """
        Wrap the gift.

        Sleeps for the time to wrap the gift.
        """
        print("Wrapping gift...")
        sleep(self.compute_time())
