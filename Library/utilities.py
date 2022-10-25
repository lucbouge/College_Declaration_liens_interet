import re
from Library.survey import table


def split_names(h1):
    assert h1 is not None
    name = h1.strip()
    assert name.count(",") == 1, name
    (lastname, firstname) = name.split(",")
    lastname = lastname.strip().title()
    firstname = firstname.strip().title()
    return (firstname, lastname)


def normalize(s):
    assert isinstance(s, str), s
    s = re.sub(r"\s+", " ", s).strip()
    return s


def check_df(df):
    for (group, grouped_df) in df.groupby(by=["firstname", "lastname"]):
        for (block, item) in table.items():
            # description = item["description"]
            questions = set(item["questions"])
            tags = set(grouped_df[grouped_df["h2"] == block]["question"])
            assert tags <= questions, (group, block, tags - questions)
