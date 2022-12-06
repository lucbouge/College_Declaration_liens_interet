def extend_key_to_answer_dict(*, new_persons, key_to_answer_dict):
    for (firstname, lastname) in new_persons:
        print(f"New person: {firstname} {lastname}")
        for (k, v) in (("Votre prénom", firstname), ("Votre nom de famille", lastname)):
            key = (
                firstname,
                lastname,
                "Données générales",
                None,
                k,
            )
            assert key not in key_to_answer_dict
            key_to_answer_dict[key] = v
    return key_to_answer_dict


def make_key_to_answer_dict(items):
    key_to_answer_dict = dict()
    for item in items:
        key = (item.firstname, item.lastname, item.h2, item.h3, item.question)
        assert key not in key_to_answer_dict, key
        key_to_answer_dict[key] = item.answer
    return key_to_answer_dict


def get_answer(*, firstname, lastname, h2, h3, question, key_to_answer_dict):
    key = (firstname, lastname, h2, h3, question)
    return key_to_answer_dict.get(key, "")
