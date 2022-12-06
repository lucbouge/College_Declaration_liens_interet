from Libraries.Config.packages import *

## https://github.com/mwilliamson/python-mammoth#readme
import mammoth

# from Libraries.Helpers.survey import persons
# from Libraries.Helpers.documents import make_documents
# from Libraries.Helpers.items import make_items, Item
# from Libraries.Utilities.utilities import check_df
# from Libraries.Helpers.answers import make_key_to_answer_dict, extend_key_to_answer_dict

completed_docx_patttern = "Declarations/Etat_final/Declarations_mises_a_jour/*.docx"


def main():
    for path in glob.glob(completed_docx_patttern):
        suffix = pathlib.Path(path).suffix.lower()
        assert suffix == ".docx", suffix
        basename = os.path.basename(path)
        with open(path, "rb") as cin:
            result = mammoth.convert_to_html(cin)
            text = result.value
            text = "<html><body>" + text + "</body></html>"
            soup = BeautifulSoup(text, features="lxml")
            process(soup=soup, basename=basename)


def process(*, soup, basename):
    print(f"\n\n===================== {basename}\n\n")
