"""
Solution to the CodeWars kata Pagination Helper
Link:
https://www.codewars.com/kata/515bb423de843ea99400000a
"""
from math import ceil


class PaginationHelper:
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.items = collection
        self.items_per_page = items_per_page
        self.pages = ceil(len(collection) / self.items_per_page)

    # returns the number of pages
    def page_count(self):
        return self.pages

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.items)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= self.pages:
            return -1
        if page_index != self.pages - 1:
            return self.items_per_page
        return len(self.items) % self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index >= len(self.items) or item_index < 0:
            return -1
        return item_index // self.items_per_page


if __name__ == '__main__':
    helper = PaginationHelper(range(1, 25), 10)
    print(f'Page Count: {helper.page_count()}')
    print(f'Page Index: {helper.page_index(-23)}')
    print(f'Item Count: {helper.item_count()}')
    print(f'Page Item Count: {helper.page_item_count(2)}')
