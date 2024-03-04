class Handsign:

    def __init__(self, value, **naming):
        self.value = value

        self.name = self.val2 = naming.get('name', 'undefined')
        self.character = naming.get('character', 'u')

    def __str__(self):
        return str(self.value)

    def compare(self, val_extern):
        # a handsign beats another one, when their difference % 5 equal 1 or 3
        diff = (val_extern - self.value) % 5

        if (diff == 1) | (diff == 3):
            return 1  # this sign beats another one
        elif diff == 0:
            return 0  # same sign
        else:
            return -1  # this sign lost to another one
