from Libraries.Config.packages import *

## https://github.com/mwilliamson/python-mammoth#readme
import mammoth

from Libraries.Helpers.survey import persons
from Libraries.Helpers.documents import make_documents
from Libraries.Helpers.items import make_items, Item
from Libraries.Utilities.utilities import check_df
from Libraries.Helpers.answers import make_key_to_answer_dict, extend_key_to_answer_dict

original_docx_filename = "Sources/2021-11-23_results.docx"
# original_docx_filename = "test.docx"


################################################################################


def main():
    with open(original_docx_filename, "rb") as cin:
        result = mammoth.convert_to_html(cin)
        text = result.value
        text = "<html><body>" + text + "</body></html>"
    with open("output.html", "w") as cout:
        cout.write(text)
    ##
    soup = BeautifulSoup(text, features="lxml")
    items = make_items(soup=soup)
    # pp.pprint(items)
    ##
    df = pd.DataFrame.from_records(items, columns=Item._fields)
    # df.to_excel("results.xlsx", index=False)
    check_df(df)
    ##
    key_to_answer_dict = make_key_to_answer_dict(items)
    existing_persons = set((item.firstname, item.lastname) for item in items)
    new_persons = set(persons) - existing_persons
    key_to_answer_dict = extend_key_to_answer_dict(
        new_persons=new_persons, key_to_answer_dict=key_to_answer_dict
    )
    ##
    make_documents(
        key_to_answer_dict=key_to_answer_dict,
        persons=persons,
    )


main()
