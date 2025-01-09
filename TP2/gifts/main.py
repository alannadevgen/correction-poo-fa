from gift import Gift
from sleigh import Sleigh

if __name__ == "__main__":
    # Creating gifts
    gift_mum = Gift("medium")
    gift_dad = Gift("small")
    gift_daughter = Gift("small")
    gift_son = Gift("large")
    gift_aunt = Gift("medium")
    gift_uncle = Gift("large")
    gift_grandma = Gift("small")

    # Creating sleigh
    sleigh = Sleigh(20)

    # Adding gifts to sleigh
    sleigh.add_gift(gift_mum)
    sleigh.add_gift(gift_dad)
    sleigh.add_gift(gift_daughter)
    sleigh.add_gift(gift_son)
    sleigh.add_gift(gift_aunt)
    sleigh.add_gift(gift_uncle)
    sleigh.add_gift(gift_grandma)

    # Removing gifts from sleigh
    sleigh.remove_gift(gift_dad)

    # Printing gifts in sleigh
    print("Gifts in sleigh:")
    for gift in sleigh.gifts:
        print(gift.size)

    # Printing free capacity
    print(f"Free capacity: {sleigh.free_capacity}")

    # Printing number of gifts in sleigh
    print(f"Number of gifts: {len(sleigh)}")

    # Comparing sleighs
    sleigh2 = Sleigh(30)
    sleigh3 = Sleigh(20)

    print(f"Sleigh 1 < Sleigh 2: {sleigh < sleigh2}")
    print(f"Sleigh 1 == Sleigh 2: {sleigh == sleigh2}")
    print(f"Sleigh 1 > Sleigh 2: {sleigh > sleigh2}")

    print(f"Sleigh 1 < Sleigh 3: {sleigh < sleigh3}")
    print(f"Sleigh 1 == Sleigh 3: {sleigh == sleigh3}")
    print(f"Sleigh 1 > Sleigh 3: {sleigh > sleigh3}")
