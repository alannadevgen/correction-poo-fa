from gift import Gift


class Sleigh:
    def __init__(self, capacity: int):
        """
        Create a sleigh.

        Attributes
        ----------
        capacity : int
            Capacity of the sleigh.
        current_capacity : int
            Current capacity of the sleigh.
        gifts : list
            List of gifts in the sleigh.
        """
        self.capacity = capacity
        self.current_capacity = 0
        self.gifts = []

    @property
    def free_capacity(self):
        """
        Compute the free capacity of the sleigh.

        Returns
        -------
        float
            Free capacity of the sleigh.
        """
        return self.capacity - self.current_capacity

    def add_gift(self, gift: Gift):
        """
        Add a gift to the sleigh.

        Parameters
        ----------
        gift : Gift
            A gift to add to the sleigh.
        """
        gift_weight = gift.compute_weight()
        if self.free_capacity >= gift_weight:
            self.gifts.append(gift)
            self.current_capacity += gift_weight
        else:
            print("Sleigh cannot carry this gift")

    def remove_gift(self, gift: Gift):
        """
        Remove a gift from the sleigh.

        Parameters
        ----------
        gift : Gift
            A gift to remove from the sleigh.
        """
        if gift in self.gifts:
            self.gifts.remove(gift)
            self.current_capacity -= gift.compute_weight()
        else:
            print("Gift not found in sleigh")

    def __len__(self):
        """Return the number of gifts in the sleigh."""
        return len(self.gifts)

    def __eq__(self, other):
        """Check if two sleighs are equal."""
        return self.capacity == other.capacity

    def __lt__(self, other):
        """Check if one sleigh has less capacity than another."""
        return self.capacity < other.capacity

    def __gt__(self, other):
        """Check if one sleigh has more capacity than another."""
        return self.capacity > other.capacity