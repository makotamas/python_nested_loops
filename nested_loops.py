# 1. feladat
m = [[1, 1, 1, 2, 1], [2, 3, 2, 2, 2], [3, 3, 2, 3, 3], [4, 4, 4, 3, 4]]

def matrix_sum(matrix):
    sum = 0
    for line in matrix:
        for element in line:
            sum += element
    return sum

sum = matrix_sum(m)
print("Az elemek összege:", sum)

# 2. feladat
cars = [
    {"price": 1549,
     "passengerQty": 4,
     "currency": "EUR",
     "type": "Kia",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 1954,
     "passengerQty": 5,
     "currency": "EUR",
     "type": "Suzuki",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 2544,
     "passengerQty": 5,
     "currency": "USD",
     "type": "Opel",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 2544,
     "passengerQty": 2,
     "currency": "USD",
     "type": "Opel",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Timea",
         "Miklos"
     ]
     },
    {"price": 9542,
     "passengerQty": 4,
     "currency": "USD",
     "type": "Ford",
     "transmission": "automatic",
     "passengers": [
         "Gabor",
         "Timea",
         "Miklos"
     ]
     },
]

def passanger_checker(cars):
    for car in cars:
        if car["passengerQty"] < len(car["passengers"]):
            print("A(z)", car["type"], "típusú autóban túl sok az utas")

passanger_checker(cars)

# 3. feladat
def price_exchanger(currency_rate):
    for car in cars:
        if car["currency"] == "EUR":
            car["price"] = int(car["price"] * currency_rate)
            car["currency"] = "USD"
            print("Autó neve:", car["type"])
            print("Ár:", car["price"], car["currency"])

currency_rate = 1.18

price_exchanger(currency_rate)

#4. feladat
persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican", "French"]

for person in persons:
    for restaurant in restaurants:
        print(person, "eats", restaurant)

#5. feladat
my_list = [[4, 5], [7, 4], [2, 5], [9, 4]]

for sublist in my_list:
    sublist.append(sublist[0] + sublist[1])

print(my_list)



