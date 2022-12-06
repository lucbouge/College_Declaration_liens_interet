from Libraries.Config.packages import *
from Libraries.Helpers.documents import set_language


## https://github.com/mwilliamson/python-mammoth#readme
import mammoth

# from Libraries.Helpers.survey import persons
# from Libraries.Helpers.documents import make_documents
# from Libraries.Helpers.items import make_items, Item
# from Libraries.Utilities.utilities import check_df
# from Libraries.Helpers.answers import make_key_to_answer_dict, extend_key_to_answer_dict

completed_docx_patttern = "Declarations/Etat_final/Declarations_mises_a_jour/*.docx"

survey_table = {
    1: {
        "title": "Données générales",
        "questions": {
            1: "Votre prénom",
            2: "Votre nom de famille",
            3: "Votre adresse électronique",
            4: "Votre affiliation principale aujourd'hui",
            5: "Votre adresse professionnelle",
            6: "Votre adresse personnelle",
            7: "Votre numéro de téléphone portable",
        },
    },
    2: {
        "title": "Activité principale",
        "questions": {
            1: "Nature de l'activité",
            2: "Activité",
            3: "Lieu d’exercice",
            4: "Début",
            5: "Fin",
        },
    },
    3: {
        "title": "Activité secondaire",
        "questions": {
            1: "Nature de l'activité",
            2: "Organisme",
            3: "Domaine et type de travaux",
            4: "Rémunération: montant et bénéficiaire",
            5: "Début",
            6: "Fin",
        },
    },
    4: {
        "title": "Activité financée",
        "questions": {
            1: "Nature de l'activité",
            2: "Structures et activités des bénéficiaires du financement",
            3: "Organisme financeur",
            4: "Pourcentage montant/budget, selon l'échelle ci-dessus",
            5: "Montant, en ordre de grandeur",
            6: "Début",
            7: "Fin",
        },
    },
    5: {
        "title": "Participation",
        "questions": {
            1: "Structure concernée",
            2: "Type d'investissement",
            3: "Part dans le capital",
            4: "Montant détenu",
            5: "Début",
            6: "Fin",
        },
    },
    6: {
        "title": "Engagement",
        "questions": {
            1: "Cadre de l'activité",
            2: "Statut dans ce cadre",
            3: "Fonctions exercées",
            4: "Début",
            5: "Fin",
        },
    },
    7: {
        "title": "Autres liens d'intérêt",
        "questions": {
            1: "Elément ou fait concerné",
            2: "Montant des sommes perçues si c'est le cas",
            3: "Commentaires",
            4: "Début",
            5: "Fin",
        },
    },
}


def main():
    data_list = get_data_list()
    data_dict = dict((data.tags, data) for data in data_list)
    check_data(data_dict=data_dict)
    document = make_document(data_dict=data_dict)
    document.save("result.docx")


################################################################################


def make_document(*, data_dict):
    document = docx.Document()
    ##
    set_language(lang="fr-FR", document=document)
    ##
    document.add_heading("Déclarations de liens d'intérêt", 0)
    now = datetime.datetime.now()
    now_string = s = now.strftime("%d/%m/%Y, %H:%M")
    document.add_paragraph(f"Date: {now_string}")
    assert document is not None
    ##
    make_data_entries(data_dict=data_dict, document=document)
    return document


################################################################################

MAX = 10


def make_data_entries(*, data_dict, document):
    n0_list = sorted(set(int(tags[0]) for tags in data_dict))
    for n0 in n0_list:
        firstname = data_dict[(n0, 1, 1, 1)].answer
        lastname = data_dict[(n0, 1, 1, 2)].answer
        document.add_page_break()
        document.add_heading(f"Personne {n0}: {lastname}, {firstname}", 1)
        print(n0, firstname, lastname)
        ##
        for n1 in range(MAX):
            if (n0, n1, 1, 1) not in data_dict:
                continue
            title = survey_table[n1]["title"]
            document.add_heading(f"Bloc {n1}: {title}", 2)
            # print(n1, title)
            ##
            for n2 in range(MAX):
                if (n0, n1, n2, 1) not in data_dict:
                    continue
                document.add_heading(f"Réponse {n2}", 3)
                ##
                for n3 in range(MAX):
                    if n3 not in survey_table[n1]["questions"]:
                        continue
                    tag = (n0, n1, n2, n3)
                    if tag not in data_dict:
                        answer = ""
                    else:
                        data = data_dict[tag]
                        data_question = data.question
                        original_question = survey_table[n1]["questions"][n3]
                        if data_question != original_question:
                            if data_question == "Rémunération montant et bénéficiaire":
                                data_question = "Rémunération: montant et bénéficiaire"
                            assert data_question == original_question, (
                                data,
                                original_question,
                            )
                        answer = data.answer
                        make_document_question(
                            tag=tag,
                            question=original_question,
                            answer=answer,
                            document=document,
                        )


def make_document_question(*, tag, question, answer, document):
    p = document.add_paragraph(style="List Bullet")
    tag_string = make_prefix_tag(tag=tag)
    p.add_run(f"{tag_string} ")
    p.add_run(f"{question}:").bold = True
    p.add_run(f" {answer}")


def make_prefix_tag(*, tag):
    assert isinstance(tag, tuple)
    assert all(isinstance(x, int) for x in tag)
    assert len(tag) == 4
    tag_string = ".".join(str(x) for x in tag)
    return f"[{tag_string}]"


################################################################################


def check_data(*, data_dict):
    for (tags, data) in data_dict.items():
        number = tags[3]
        root = tags[0:3] + (number,)
        assert root in data_dict


################################################################################


def get_data_list():
    data_list = list()
    for path in glob.glob(completed_docx_patttern):
        suffix = pathlib.Path(path).suffix.lower()
        assert suffix == ".docx", suffix
        basename = os.path.basename(path)
        with open(path, "rb") as cin:
            result = mammoth.convert_to_html(cin)
        text = result.value
        text = "<html><body>" + text + "</body></html>"
        soup = BeautifulSoup(text, features="lxml")
        new_data_list = extract_data_list(soup=soup, basename=basename)
        data_list += new_data_list
    return data_list


################################################################################


class Data(NamedTuple):
    basename: str
    tags: Tuple[int]
    question: str
    answer: str


li_pattern = re.compile(
    r"^\s*\[?(\d{1,2})\.(\d)\.(\d)\.(\d)\]\s*.*", flags=re.IGNORECASE
)


def extract_data_list(*, soup, basename):
    print(f"\n\n===================== {basename}\n\n")
    data_list = list()
    for li in soup.find_all("li"):
        m = re.fullmatch(li_pattern, li.get_text())
        if m is None:
            print(
                basename,
                li,
            )
            if li.get_text() == "OK":
                continue
            raise AssertionError(f"Unexpected li tag at {basename}: {li}")
        tags_str = m.groups()
        assert len(tags_str) == 4
        tags_int = tuple(int(x) for x in tags_str)
        ##
        question = None
        answer = None
        try:
            contents = li.contents
            assert 2 <= len(contents) <= 3, contents
            ##
            contents1 = contents[1]
            assert isinstance(contents1, Tag) and contents1.name == "strong", contents1
            question = contents1.get_text().strip()
            assert question.endswith(":"), question
            question = question[0:-1]
            # print(question)
            ##
            if len(contents) == 2:
                answer = ""
            else:
                contents2 = contents[2]
                assert isinstance(contents2, NavigableString)
                answer = contents2.strip()
        except AssertionError as e:
            if question == "Votre numéro de téléphone portable: 0638414452":
                question = "Votre numéro de téléphone portable"
                answer = "0638414452"
            elif question == "Votre adresse électronique: lena@biologie.ens.fr":
                question = "Votre adresse électronique"
                answer = "lena@biologie.ens.fr"
            else:
                raise
        ##
        data = Data(basename=basename, tags=tags_int, question=question, answer=answer)
        if len(answer) == 0:
            continue
        data_list.append(data)
    return data_list
