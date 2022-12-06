from bs4 import BeautifulSoup, Tag, PageElement, NavigableString
from typing import NamedTuple, Optional
from Library import utilities


class Item(NamedTuple):
    firstname: str
    lastname: str
    h1: str
    h2: str
    h3: Optional[str]
    question: str
    answer: str


def make_items(*, soup):
    assert soup is not None
    body = soup.body
    assert body is not None
    items = list()
    ##
    h1 = None
    h2 = None
    h3 = None
    firstname = None
    lastname = None
    for e in body.children:
        assert isinstance(e, Tag), e
        if e.name == "h1":
            assert is_pure(e)
            h1 = e.get_text()
            h2 = None
            h3 = None
            li = None
            # print(h1)
        elif e.name == "h2":
            assert is_pure(e)
            assert h1 is not None
            h2 = e.get_text()
            h3 = None
            li = None
            # print(h2)
        elif e.name == "h3":
            assert is_pure(e)
            assert h1 is not None
            assert h2 is not None
            h3 = e.get_text()
            li = None
            # print(h3)
        elif e.name == "ul":
            assert h1 is not None
            assert h2 is not None
            if h2 != "Données générales":
                assert h3 is not None, e
            else:
                assert h3 is None
                h3 = "Réponse 1"
            ul = e
            for li in ul.children:
                assert isinstance(li, Tag)
                assert is_pure(li)
                assert li.name == "li"
                item = make_item_from_li(h1=h1, h2=h2, h3=h3, li=li)
                items.append(item)
        else:
            assert isinstance(e, Tag)
            assert e.name == "p"
            assert is_pure(e)
            print(f"Ignored element: {e}")
    return items


def is_pure(e: PageElement):
    if isinstance(e, NavigableString):
        return True
    assert isinstance(e, Tag)
    for tag in e.find_all():
        if tag.name == "strong":
            continue
        raise AssertionError(f"Unexpected tag: {tag}")
    return True


################################################################################


def make_item_from_li(*, h1, h2, h3, li):
    ##
    parts = li.contents
    assert len(parts) == 2, parts
    # print(parts)
    ##
    question_part = parts[0]
    assert isinstance(question_part, Tag), question_part
    assert question_part.name == "strong", question_part
    question = question_part.get_text().strip()
    assert question.endswith(":"), question
    question = question[:-1]
    question = utilities.normalize(question)
    ##
    answer_part = parts[1]
    assert isinstance(answer_part, NavigableString), answer_part
    answer = answer_part.get_text()
    answer = utilities.normalize(answer)
    ##
    # print(question, "==>", answer)
    ##
    firstname, lastname = utilities.split_names(h1)
    item = make_item(
        firstname=firstname,
        lastname=lastname,
        h1=h1,
        h2=h2,
        h3=h3,
        question=question,
        answer=answer,
    )
    return item


def make_item(
    *,
    firstname,
    lastname,
    h1,
    h2,
    h3,
    question,
    answer,
):
    item = Item(
        firstname=firstname,
        lastname=lastname,
        h1=h1,
        h2=h2,
        h3=h3,
        question=question,
        answer=answer,
    )
    assert all(v is not None for (k, v) in item._asdict().items() if k != "h3"), item
    return item
