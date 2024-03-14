from linkedList import LinkedList
import random


def main():
    linked_list = LinkedList()

    for i in range(10):
        rand_val = random.randint(0, 100)
        linked_list.add(rand_val)

    print(len(linked_list))
    print('---')

    for item in linked_list:
        print(item)


if __name__ == '__main__':
    main()
