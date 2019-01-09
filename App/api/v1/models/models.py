import datetime
time_now = datetime.datetime.now()

User = [
    {
        "id": 1,
        "firstName": "trev",
        "lastName": "zonecc",
        "otherName": "bk",
        "userName": "zonecc",
        "email": "trevbk@gmail.com",
        "phone": "+254712345678",
        "password": "$$22BBkk",
        "confirmPassword": "$$22BBkk",
        "regDate": time_now.strftime("%D"),
        "is Admin": True
    },
    {
        "id": 2,
        "firstName": "Mary",
        "lastName": "Merry",
        "otherName": "Marry",
        "userName": "m_m_m",
        "email": "m_m_m_mm@gmail.com",
        "phone": "+254712345679",
        "password": "$$22BBkk",
        "confirmPassword": "$$22BBkk",
        "regDate": time_now.strftime("%D"),
        "is Admin": False
    }
]
