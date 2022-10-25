from Library import notices

table = {
    "Données générales": {
        "description": "Votre activité principale exercée actuellement et vos autres activités principales éventuelles au cours des 5 dernières années",
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
        "description": notices.notice_actvites_secondaires,
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
        "description": notices.notice_enseignement,
        "questions": (
            "Cadre de l'activité",
            "Statut dans ce cadre",
            "Fonctions exercées",
            "Début",
            "Fin",
        ),
    },
    "Autres liens": {
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
