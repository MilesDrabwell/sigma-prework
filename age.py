from datetime import date, datetime


def age_calc(born):
    born_date = datetime.strptime(str(born), "%d-%m-%Y")
    today = date.today()
    age = today.year - born_date.year
    if born_date.month > today.month:
        age -= 1
    elif born_date.month == today.month and born_date.day > today.day:
        age -= 1
    return age
