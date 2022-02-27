import random


def random_letter():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    return alphabet[ random.randint(0,len(alphabet)-1) ]

def random_text(length):
    random_string = ""
    for i in range(length):
        random_string += random_letter()
    return random_string

print(random_text(10))

def random_text_print(length):
    random_string = ""
    for i in range(length):
        random_string += random_letter()
    print(random_string)

cs_dept_phonebook = { 
                        "Porter"  : "3041",
                        "Case"    : "4618",
                        "Manley"  : "2177",
                        "Urness"  : "2188",
                        "Rieck"   : "3795"
                    }

print(cs_dept_phonebook["Manley"])


covid_data = {'ID': 'd884fba6-4faf-4234-8205-5f9710885b3e',
 'Message': '',
 'Global': {'NewConfirmed': 1021332,
            'TotalConfirmed': 427288052,
            'NewDeaths': 7936,
            'TotalDeaths': 5902846,
            'NewRecovered': 0,
            'TotalRecovered': 0,
            'Date': '2022-02-23T17:48:41.476Z'},
 'Countries': [{'ID': '8dca8226-2ffa-4f04-af28-579f9ecf8809',
                'Country': 'Afghanistan',
                'CountryCode': 'AF',
                'Slug': 'afghanistan',
                'NewConfirmed': 0,
                'TotalConfirmed': 172716,
                'NewDeaths': 0,
                'TotalDeaths': 7569,
                'NewRecovered': 0,
                'TotalRecovered': 0,
                'Date': '2022-02-23T17:48:41.476Z',
                'Premium': {}},
               {'ID': '9e146d7b-db66-421e-af5c-a22c0b86aef2',
                'Country': 'Albania',
                'CountryCode': 'AL',
                'Slug': 'albania',
                'NewConfirmed': 0,
                'TotalConfirmed': 270455,
                'NewDeaths': 0,
                'TotalDeaths': 3451,
                'NewRecovered': 0,
                'TotalRecovered': 0,
                'Date': '2022-02-23T17:48:41.476Z',
                'Premium': {}},
               {'ID': '9839f220-e32a-4352-b3ba-9a995029f8ff',
                'Country': 'Algeria',
                'CountryCode': 'DZ',
                'Slug': 'algeria',
                'NewConfirmed': 0,
                'TotalConfirmed': 264365,
                'NewDeaths': 0,
                'TotalDeaths': 6812,
                'NewRecovered': 0,
                'TotalRecovered': 0,
                'Date': '2022-02-23T17:48:41.476Z',
                'Premium': {}},
               {'ID': 'e80e0aaf-9a7a-455f-89e3-367b91641c18',
                'Country': 'Andorra',
                'CountryCode': 'AD',
                'Slug': 'andorra',
                'NewConfirmed': 0,
                'TotalConfirmed': 37820,
                'NewDeaths': 0,
                'TotalDeaths': 151,
                'NewRecovered': 0,
                'TotalRecovered': 0,
                'Date': '2022-02-23T17:48:41.476Z',
                'Premium': {}},
               {'ID': 'c7c4a10e-efbb-46af-af55-37647d958d9c',
                'Country': 'Angola',
                'CountryCode': 'AO',
                'Slug': 'angola',
                'NewConfirmed': 0,
                'TotalConfirmed': 98671,
                'NewDeaths': 0,
                'TotalDeaths': 1899,
                'NewRecovered': 0,
                'TotalRecovered': 0,
                'Date': '2022-02-23T17:48:41.476Z',
                'Premium': {}}],
 'Date': '2022-02-23T17:48:41.476Z'}    
# print(type(covid_data))
# for x in covid_data:
#     print(x,type(covid_data[x]))
# for y in covid_data["Countries"][0]:
#     print(y)
x = covid_data["Countries"][2]
print(x["Country"], x["TotalConfirmed"])