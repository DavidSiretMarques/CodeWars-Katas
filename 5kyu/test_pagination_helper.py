import pytest
import pagination_helper as pg


@pytest.mark.parametrize('collection, items_per_page',
                         [(range(25), 10),
                          (range(5), 10),
                          (range(5), 1),
                          (range(21), 3)])
def test_init(collection, items_per_page):
    helper = pg.PaginationHelper(collection, items_per_page)
    assert isinstance(helper, pg.PaginationHelper)


@pytest.fixture
def pagination_helper():
    return pg.PaginationHelper(range(25), 10)


def test_has_3_pages(pagination_helper):
    assert pagination_helper.pages == 3


def test_has_24_items(pagination_helper):
    assert pagination_helper.items == range(25)


def test_has_10_items_per_page(pagination_helper):
    assert pagination_helper.items_per_page == 10


def test_page_count_method(pagination_helper):
    assert pagination_helper.page_count() == 3


def test_item_count_method(pagination_helper):
    assert pagination_helper.item_count() == 25


@pytest.mark.parametrize("page_index,page_item_num",
                         [(0, 10),
                          (2, 5),
                          (15, -1)])
def test_page_item_count_method(pagination_helper, page_index, page_item_num):
    assert pagination_helper.page_item_count(page_index) == page_item_num


@pytest.mark.parametrize("item_index,page_num",
                         [(0, 0),
                          (2, 0),
                          (15, 1),
                          (23, 2),
                          (50, -1)])
def test_page_index_method(pagination_helper, item_index, page_num):
    assert pagination_helper.page_index(item_index) == page_num
