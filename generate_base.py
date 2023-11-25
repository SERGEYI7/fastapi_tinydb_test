import requests

users = [
  {"name": "Иванов Иван", "email": "ivanov@example.com", "phone": "+9876543210", "text": "Пример текста 1", "date": "01.12.2023"},
  {"name": "Петров Петр", "email": "petrov@example.com", "phone": "+1234567890", "text": "Пример текста 2", "date": "05.11.2023"},
  {"name": "Сидорова Анна", "email": "sidorova@example.com", "phone": "+5556667777", "text": "Пример текста 3", "date": "18.09.2023"},
  {"name": "Козлова Елена", "email": "kozlova@example.com", "phone": "+9876543210", "text": "Пример текста 4", "date": "22.08.2023"},
  {"name": "Григорьев Игорь", "email": "grigorev@example.com", "phone": "+1234567890", "text": "Пример текста 5", "date": "07.07.2023"},
  {"name": "Орлова Мария", "email": "orlova@example.com", "phone": "+5556667777", "text": "Пример текста 6", "date": "14.06.2023"},
  {"name": "Александров Александр", "email": "alexandrov@example.com", "phone": "+9876543210", "text": "Пример текста 7", "date": "29.04.2023"},
  {"name": "Егоров Егор", "email": "egorov@example.com", "phone": "+1234567890", "text": "Пример текста 8", "date": "03.03.2023"},
  {"name": "Татьянова Татьяна", "email": "tatyanova@example.com", "phone": "+5556667777", "text": "Пример текста 9", "date": "12.02.2023"},
  {"name": "Дмитриев Дмитрий", "email": "dmitriev@example.com", "phone": "+9876543210", "text": "Пример текста 10", "date": "25.01.2023"},
  {"name": "Натальина Наталья", "email": "natalina@example.com", "phone": "+1234567890", "text": "Пример текста 11", "date": "08.12.2022"},
  {"name": "Романов Роман", "email": "romanov@example.com", "phone": "+5556667777", "text": "Пример текста 12", "date": "17.11.2022"},
  {"name": "Юлиана Юлия", "email": "yuliana@example.com", "phone": "+9876543210", "text": "Пример текста 13", "date": "30.10.2022"},
  {"name": "Владимиров Владимир", "email": "vladimirov@example.com", "phone": "+1234567890", "text": "Пример текста 14", "date": "04.09.2022"},
  {"name": "Евгения Евгений", "email": "evgenia@example.com", "phone": "+5556667777", "text": "Пример текста 15", "date": "21.08.2022"},
  {"name": "Олеговна Ольга", "email": "olegova@example.com", "phone": "+9876543210", "text": "Пример текста 16", "date": "26.07.2022"},
  {"name": "Степанов Степан", "email": "stepanov@example.com", "phone": "+1234567890", "text": "Пример текста 17", "date": "09.06.2022"},
  {"name": "Андреев Андрей", "email": "andreev@example.com", "phone": "+5556667777", "text": "Пример текста 18", "date": "14.05.2022"},
  {"name": "Нина Николаевна", "email": "nina@example.com", "phone": "+9876543210", "text": "Пример текста 19", "date": "27.04.2022"},
  {"name": "Максимов Максим", "email": "maximov@example.com", "phone": "+1234567890", "text": "Пример текста 20", "date": "02.03.2022"}
]

for user in users:
    re = requests.post("http://127.0.0.1:8000/set_users", json=user)
    print(re.text)
