from Library import notices

structure = {
    "Données générales": {
        "nb_answers": 1,
        "description": notices.notice_donnees_generales,
        "questions": (
            "Votre prénom",
            "Votre nom de famille",
            "Votre adresse électronique",
            "Votre affiliation principale aujourd'hui",
            "Votre adresse professionnelle",
            "Votre adresse personnelle",
            "Votre numéro de téléphone portable",
        ),
    },
    "Activité principale": {
        "nb_answers": 4,
        "description": notices.notice_activite_principale,
        "questions": (
            "Nature de l'activité",
            "Activité",
            "Lieu d’exercice",
            "Début",
            "Fin",
        ),
    },
    "Activité secondaire": {
        "nb_answers": 6,
        "description": notices.notice_activites_secondaires,
        "questions": (
            "Nature de l'activité",
            "Organisme",
            "Domaine et type de travaux",
            "Rémunération: montant et bénéficiaire",
            "Début",
            "Fin",
        ),
    },
    "Activité financée": {
        "nb_answers": 4,
        "description": notices.notice_activite_financee,
        "questions": (
            "Nature de l'activité",
            "Structures et activités des bénéficiaires du financement",
            "Organisme financeur",
            "Pourcentage montant/budget, selon l'échelle ci-dessus",
            "Montant, en ordre de grandeur",
            "Début",
            "Fin",
        ),
    },
    "Participation": {
        "nb_answers": 4,
        "description": notices.notice_participation,
        "questions": (
            "Structure concernée",
            "Type d'investissement",
            "Part dans le capital",
            "Montant détenu",
            "Debut",
            "Fin",
        ),
    },
    "Engagement": {
        "nb_answers": 4,
        "description": notices.notice_engagement,
        "questions": (
            "Cadre de l'activité",
            "Statut dans ce cadre",
            "Fonctions exercées",
            "Début",
            "Fin",
        ),
    },
    "Autres liens": {
        "nb_answers": 4,
        "description": notices.notice_autres,
        "questions": (
            "Elément ou fait concerné",
            "Montant des sommes perçues si c'est le cas",
            "Commentaires",
            "Début",
            "Fin",
        ),
    },
}

persons = (
    ("Éric", "Arquis"),
    ("Luc", "Bougé"),
    ("Anne", "Guillaume"),
    ("Louise", "Nyssen"),
    ("Marc", "Taillefer"),
    ("Guy", "Wormser"),
    ##
    ("Bruno", "Allard"),
    ("Patrick", "Lemaire"),
    ("Clément", "Léna"),
    ("François", "Massol"),
    ("Rémi", "Mounier"),
    ("Benoît", "Schoefs"),
    ##
    ("Magali", "Boutrais"),
    ("Florence", "Hachez-Leroy"),
    ("Marie-Pierre", "Julien"),
    ("Pierre", "Lurbe"),
    ("Sylvie", "Pittia"),
    ("Dominique", "Valérian"),
    ##
    ("Claire", "Dupas"),
)
