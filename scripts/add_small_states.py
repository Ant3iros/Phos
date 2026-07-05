"""Add small island states and micro-states to default_2016.json (Comores, Cap-Vert, etc.)."""
import json
import os

SCENARIO_PATH = os.path.join(os.path.dirname(__file__), '..', 'backend', 'app', 'data', 'scenarios', 'default_2016.json')


def country(cid, name, flag, capital, continent, pop, gov, ideology, leader,
            gdp, gdp_pc, growth, inflation, unemployment, debt, currency,
            sectors_main, sectors_pct, mil_strength, mil_personnel, defense_pct,
            nat_stats, relations, traits, description, color, stability=55):
    return {
        "id": cid, "name": name, "flag": flag, "capital": capital, "continent": continent,
        "population": pop, "government_type": gov, "ideology": ideology, "leader": leader,
        "alliances": [],
        "economy": {
            "gdp": gdp, "gdp_per_capita": gdp_pc, "gdp_growth": growth,
            "inflation": inflation, "unemployment": unemployment, "debt_pct_gdp": debt,
            "currency": currency, "main_sectors": sectors_main, "sectors": sectors_pct,
        },
        "military": {
            "strength": mil_strength, "active_personnel": mil_personnel,
            "nuclear_weapons": False, "defense_budget_pct": defense_pct,
            "equipment": {"chars_combat": 0, "avions_chasse": 0, "navires_guerre": 0,
                          "sous_marins": 0, "helicopteres": 2, "artillerie": 4},
        },
        "national_stats": nat_stats,
        "relations": relations,
        "personality_traits": traits,
        "description": description,
        "color": color,
        "initial_stability": stability,
    }


NEW_COUNTRIES = {
    "COM": country(
        "COM", "Comores", "🇰🇲", "Moroni", "Afrique", 796000,
        "présidentiel", "démocratie_fragile", "Azali Assoumani",
        1.0, 1300, 2.2, 1.8, 20.0, 27.0, "KMF",
        ["agriculture", "vanille", "ylang-ylang", "pêche"],
        {"agriculture": 47.0, "industrie": 12.0, "services": 41.0},
        1, 500, 1.0,
        {"sovereignty": 40.0, "food_autonomy": 60.0, "energy_autonomy": 15.0, "economic_independence": 20.0},
        {"FRA": 40, "MDG": 35, "TZA": 30, "SAU": 25, "CHN": 20},
        ["fragile", "insulaire", "dépendant_aide"],
        "Archipel de l'océan Indien marqué par une histoire de coups d'État, les Comores dépendent de l'agriculture d'exportation et de la diaspora. Revendique Mayotte, restée française.",
        "#3d8b37", 40),
    "CPV": country(
        "CPV", "Cap-Vert", "🇨🇻", "Praia", "Afrique", 540000,
        "parlementaire", "démocratie_libérale", "Jorge Carlos Fonseca",
        1.6, 3000, 3.9, 1.4, 12.2, 126.0, "CVE",
        ["tourisme", "services", "pêche", "transferts_diaspora"],
        {"agriculture": 9.0, "industrie": 18.0, "services": 73.0},
        1, 1200, 0.6,
        {"sovereignty": 60.0, "food_autonomy": 20.0, "energy_autonomy": 25.0, "economic_independence": 30.0},
        {"PRT": 65, "USA": 45, "BRA": 40, "SEN": 35, "CHN": 25},
        ["stable", "démocratique", "insulaire"],
        "Archipel atlantique lusophone, le Cap-Vert est l'une des démocraties les plus stables d'Afrique, tournée vers le tourisme et sa diaspora.",
        "#1e40af", 72),
    "MUS": country(
        "MUS", "Maurice", "🇲🇺", "Port-Louis", "Afrique", 1263000,
        "parlementaire", "démocratie_libérale", "Anerood Jugnauth",
        12.2, 9600, 3.8, 1.0, 7.3, 65.0, "MUR",
        ["tourisme", "finance", "textile", "sucre"],
        {"agriculture": 4.0, "industrie": 22.0, "services": 74.0},
        1, 2000, 0.2,
        {"sovereignty": 65.0, "food_autonomy": 30.0, "energy_autonomy": 20.0, "economic_independence": 55.0},
        {"IND": 60, "FRA": 50, "GBR": 45, "ZAF": 40, "CHN": 35},
        ["stable", "commerçant", "diplomate"],
        "Île prospère de l'océan Indien, Maurice s'est diversifiée du sucre vers la finance offshore et le tourisme. Revendique l'archipel des Chagos face au Royaume-Uni.",
        "#dc2626", 78),
    "SYC": country(
        "SYC", "Seychelles", "🇸🇨", "Victoria", "Afrique", 94000,
        "présidentiel", "démocratie_libérale", "James Michel",
        1.4, 15000, 4.5, -1.0, 4.0, 65.0, "SCR",
        ["tourisme", "pêche", "finance_offshore"],
        {"agriculture": 2.5, "industrie": 13.5, "services": 84.0},
        1, 400, 1.3,
        {"sovereignty": 55.0, "food_autonomy": 25.0, "energy_autonomy": 15.0, "economic_independence": 40.0},
        {"IND": 50, "FRA": 45, "GBR": 40, "CHN": 30, "ARE": 35},
        ["insulaire", "touristique", "stable"],
        "Micro-État de 115 îles, les Seychelles vivent du tourisme haut de gamme et de la pêche au thon, tout en luttant contre la piraterie dans l'océan Indien.",
        "#0ea5e9", 70),
    "STP": country(
        "STP", "São Tomé-et-Príncipe", "🇸🇹", "São Tomé", "Afrique", 200000,
        "semi_présidentiel", "démocratie_fragile", "Evaristo Carvalho",
        0.35, 1750, 4.0, 5.4, 13.5, 93.0, "STD",
        ["cacao", "agriculture", "pêche", "aide_internationale"],
        {"agriculture": 12.0, "industrie": 15.0, "services": 73.0},
        1, 300, 0.8,
        {"sovereignty": 40.0, "food_autonomy": 45.0, "energy_autonomy": 10.0, "economic_independence": 18.0},
        {"PRT": 60, "AGO": 45, "GAB": 35, "BRA": 30, "CHN": 25},
        ["fragile", "insulaire", "dépendant_aide"],
        "Petit archipel du golfe de Guinée, ancien comptoir cacaoyer portugais, qui espère des découvertes pétrolières offshore.",
        "#16a34a", 55),
    "MDV": country(
        "MDV", "Maldives", "🇲🇻", "Malé", "Asie", 428000,
        "présidentiel", "islamisme_modéré", "Abdulla Yameen",
        4.2, 9800, 6.2, 0.5, 5.2, 60.0, "MVR",
        ["tourisme", "pêche", "construction"],
        {"agriculture": 3.0, "industrie": 16.0, "services": 81.0},
        1, 3000, 1.0,
        {"sovereignty": 50.0, "food_autonomy": 15.0, "energy_autonomy": 10.0, "economic_independence": 35.0},
        {"IND": 45, "CHN": 40, "SAU": 40, "LKA": 45, "USA": 20},
        ["insulaire", "touristique", "vulnérable_climat"],
        "Archipel de l'océan Indien menacé par la montée des eaux, tiraillé entre l'influence indienne et chinoise, et vivant du tourisme de luxe.",
        "#0891b2", 55),
    "MLT": country(
        "MLT", "Malte", "🇲🇹", "La Valette", "Europe", 434000,
        "parlementaire", "démocratie_libérale", "Joseph Muscat",
        11.0, 25300, 5.5, 0.9, 4.7, 58.0, "EUR",
        ["services_financiers", "tourisme", "jeux_en_ligne", "transport_maritime"],
        {"agriculture": 1.4, "industrie": 12.0, "services": 86.6},
        1, 1900, 0.5,
        {"sovereignty": 55.0, "food_autonomy": 20.0, "energy_autonomy": 15.0, "economic_independence": 50.0},
        {"ITA": 60, "GBR": 55, "FRA": 45, "DEU": 45, "LBY": 20, "TUN": 30},
        ["européen", "commerçant", "neutre"],
        "Plus petit État de l'Union européenne, Malte est un hub financier et maritime méditerranéen, en première ligne des routes migratoires.",
        "#b91c1c", 75),
    "SGP": country(
        "SGP", "Singapour", "🇸🇬", "Singapour", "Asie", 5607000,
        "parlementaire", "autoritarisme_libéral", "Lee Hsien Loong",
        318.0, 56700, 2.4, -0.5, 2.1, 112.0, "SGD",
        ["finance", "commerce", "électronique", "raffinage", "port"],
        {"agriculture": 0.0, "industrie": 26.0, "services": 74.0},
        4, 72000, 3.4,
        {"sovereignty": 75.0, "food_autonomy": 10.0, "energy_autonomy": 5.0, "economic_independence": 70.0},
        {"USA": 60, "CHN": 45, "MYS": 40, "IDN": 40, "JPN": 55, "AUS": 55, "IND": 45, "GBR": 50},
        ["pragmatique", "commerçant", "stratège", "technocratique"],
        "Cité-État hyper-développée au carrefour des routes maritimes mondiales, Singapour compense sa taille minuscule par une armée moderne, une diplomatie habile et une économie de premier plan.",
        "#e11d48", 85),
    "BHR": country(
        "BHR", "Bahreïn", "🇧🇭", "Manama", "Moyen-Orient", 1425000,
        "monarchie_absolue", "monarchie_du_golfe", "Hamad ben Issa Al Khalifa",
        32.2, 22600, 3.2, 2.8, 4.0, 81.0, "BHD",
        ["finance", "pétrole", "aluminium", "tourisme"],
        {"agriculture": 0.3, "industrie": 39.0, "services": 60.7},
        2, 8200, 4.6,
        {"sovereignty": 45.0, "food_autonomy": 10.0, "energy_autonomy": 80.0, "economic_independence": 50.0},
        {"SAU": 75, "ARE": 65, "USA": 60, "GBR": 50, "IRN": -50, "QAT": 20, "KWT": 55},
        ["pro_occidental", "monarchique", "dépendant_saoudien"],
        "Petit royaume insulaire du Golfe, siège de la Ve flotte américaine, marqué par les tensions entre la monarchie sunnite et la majorité chiite depuis 2011.",
        "#be123c", 50),
    "BRN": country(
        "BRN", "Brunei", "🇧🇳", "Bandar Seri Begawan", "Asie", 423000,
        "monarchie_absolue", "monarchie_islamique", "Hassanal Bolkiah",
        11.4, 27000, -2.5, -0.7, 6.9, 3.0, "BND",
        ["pétrole", "gaz", "services_publics"],
        {"agriculture": 1.2, "industrie": 56.6, "services": 42.2},
        2, 7200, 2.9,
        {"sovereignty": 70.0, "food_autonomy": 20.0, "energy_autonomy": 100.0, "economic_independence": 60.0},
        {"MYS": 50, "SGP": 55, "IDN": 45, "GBR": 55, "CHN": 30, "USA": 40},
        ["monarchique", "rentier", "discret"],
        "Sultanat pétrolier de Bornéo, richissime et paisible, dirigé d'une main ferme par l'une des plus anciennes monarchies au monde.",
        "#facc15", 75),
    "FJI": country(
        "FJI", "Fidji", "🇫🇯", "Suva", "Océanie", 899000,
        "parlementaire", "démocratie_fragile", "Frank Bainimarama",
        4.7, 5200, 2.4, 3.9, 5.5, 47.0, "FJD",
        ["tourisme", "sucre", "pêche", "textile"],
        {"agriculture": 13.5, "industrie": 17.4, "services": 69.1},
        1, 3500, 1.6,
        {"sovereignty": 60.0, "food_autonomy": 55.0, "energy_autonomy": 30.0, "economic_independence": 40.0},
        {"AUS": 45, "NZL": 45, "CHN": 35, "IND": 40, "USA": 35},
        ["insulaire", "vulnérable_climat", "post_putsch"],
        "Principal archipel du Pacifique Sud, les Fidji sortent d'une série de coups d'État et jouent l'équilibre entre l'Australie, la Chine et l'Inde.",
        "#67e8f9", 58),
    "PNG": country(
        "PNG", "Papouasie-Nouvelle-Guinée", "🇵🇬", "Port Moresby", "Océanie", 8085000,
        "parlementaire", "démocratie_fragile", "Peter O'Neill",
        20.0, 2500, 2.0, 6.7, 2.5, 33.0, "PGK",
        ["mines", "gaz_naturel", "agriculture", "forêts"],
        {"agriculture": 22.1, "industrie": 42.9, "services": 35.0},
        1, 3600, 0.4,
        {"sovereignty": 55.0, "food_autonomy": 75.0, "energy_autonomy": 70.0, "economic_independence": 35.0},
        {"AUS": 60, "NZL": 45, "IDN": 30, "CHN": 30, "USA": 35, "JPN": 40},
        ["fragile", "riche_en_ressources", "fragmenté"],
        "État le plus peuplé du Pacifique insulaire, immensément riche en ressources mais fragmenté en centaines de groupes linguistiques, avec une question autonomiste à Bougainville.",
        "#d97706", 48),
    "TLS": country(
        "TLS", "Timor oriental", "🇹🇱", "Dili", "Asie", 1269000,
        "semi_présidentiel", "démocratie_fragile", "Taur Matan Ruak",
        1.4, 1100, 5.0, -1.3, 11.0, 8.0, "USD",
        ["pétrole", "café", "agriculture", "aide_internationale"],
        {"agriculture": 17.0, "industrie": 57.0, "services": 26.0},
        1, 2000, 1.5,
        {"sovereignty": 50.0, "food_autonomy": 50.0, "energy_autonomy": 85.0, "economic_independence": 25.0},
        {"IDN": 30, "AUS": 45, "PRT": 55, "CHN": 25, "USA": 30},
        ["jeune_état", "fragile", "dépendant_pétrole"],
        "Plus jeune nation d'Asie, indépendante de l'Indonésie depuis 2002, le Timor oriental dépend presque entièrement de son fonds pétrolier.",
        "#991b1b", 50),
}


def main():
    with open(SCENARIO_PATH, encoding="utf-8") as f:
        data = json.load(f)

    added = []
    for cid, c in NEW_COUNTRIES.items():
        if cid in data["countries"]:
            continue
        data["countries"][cid] = c
        added.append(cid)
        # Mirror relations onto existing countries
        for other_id, score in c["relations"].items():
            other = data["countries"].get(other_id)
            if other is not None:
                other.setdefault("relations", {}).setdefault(cid, score)

    with open(SCENARIO_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Added {len(added)} countries: {', '.join(added)}")
    print(f"Total countries: {len(data['countries'])}")


if __name__ == "__main__":
    main()
