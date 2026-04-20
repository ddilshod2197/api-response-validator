import requests

def tekshirish(api_url, metod, shartlar):
    try:
        response = requests.request(metod, api_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Xatolik: {e}")
        return False

    for shart in shartlar:
        if not shart(response.json()):
            print(f"Shart o'rinbosar: {shart.__name__}")
            return False

    return True

def shart1(response):
    return response['status'] == 200

def shart2(response):
    return response['data']['name'] == 'John'

def shart3(response):
    return response['data']['age'] > 18

api_url = 'https://jsonplaceholder.typicode.com/todos/1'
metod = 'GET'
shartlar = [shart1, shart2, shart3]

if tekshirish(api_url, metod, shartlar):
    print("API response tekshirildi va shartlar bajarildi.")
else:
    print("API response tekshirildi, lekin shartlar bajarmadi.")
```

Kodda quyidagi funksiyalar mavjud:

- `tekshirish()`: API response ni tekshirish uchun funksiya. Ushbu funksiya API ga request yuboradi, response ni tekshiradi va shartlarni tekshiradi.
- `shart1()`, `shart2()`, `shart3()`: API response ga shartlarni tekshirish uchun funksiyalar. Ushbu funksiyalar response ni tekshirib, shartlarni tekshiradi.
