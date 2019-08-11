from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    data = data.splitlines()
    data = data[1:]
    countries = defaultdict(list)
    for line in data:
      last_name, first_name, country_code = line.split(sep=',')
      countries[country_code].append(first_name + ' ' + last_name)
    return countries
