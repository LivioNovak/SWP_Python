from collections.abc import Iterator


class LinkedList(Iterator):

    def __init__(self):
        self.head = None

    # def __iter__ gets handled by Iterator-class

    def __next__(self):
        if self.head is not None:
            value = self.head.value
            self.head = self.head.next_item
            return value
        else:
            raise StopIteration

    def add(self, val):
        new_item = Item(val)
        # when list is empty, new item is head
        if self.head is None:
            self.head = new_item
        # otherwise, set new item as "next" in currently last
        else:
            prev = self.get_last()
            prev.set_next(new_item)

    def get_last(self):
        item = self.head
        # raise exception when list is empty
        if item is None:
            raise Exception

        # return last item otherwise
        while item.get_next() is not None:
            item = item.get_next()

        return item

    def __len__(self):
        if self.head is not None:
            size = 1
            item = self.head
            while item.get_next() is not None:
                size += 1
                item = item.get_next()

            return size

        else:
            return 0


class Item:

    def __init__(self, val):
        self.value = val
        self.next_item = None

    def set_next(self, item):
        self.next_item = item

    def get_next(self):
        return self.next_item

    def __str__(self):
        return f'Item: {self.value}'
