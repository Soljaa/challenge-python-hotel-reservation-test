import re


# Classe hotel com método para saber o valor total para as datas
class Hotel:
    week_days = ['mon', 'tues', 'wed', 'thur', 'fri']
    hotels = {}  # Dicionário como atributo de classe para guardar os nomes de instâncias Hotel e seus ratings

    def __init__(self,
                 name,
                 rating,
                 regular_week_price,
                 regular_weekend_price,
                 reward_week_price,
                 reward_weekend_price):
        self.name = name
        self.rating = rating
        self.regular_week_price = regular_week_price
        self.regular_weekend_price = regular_weekend_price
        self.reward_week_price = reward_week_price
        self.reward_weekend_price = reward_weekend_price
        Hotel.hotels[self.name] = self.rating

    def get_total_price(self, client, reservation):
        total_price = 0
        if client == 'Regular':
            for day in reservation:
                if day in Hotel.week_days:
                    total_price += float(self.regular_week_price)
                else:
                    total_price += float(self.regular_weekend_price)
        elif client == 'Rewards' or 'Reward':
            for day in reservation:
                if day in Hotel.week_days:
                    total_price += float(self.reward_week_price)
                else:
                    total_price += float(self.reward_weekend_price)
        return total_price

    @classmethod
    def get_hotel(cls):
        return cls.hotels


def get_cheapest_hotel(entry):   #DO NOT change the function's name
    Lakewood = Hotel('Lakewood', 3, 110, 90, 80, 80)
    Bridgewood = Hotel('Bridgewood', 4, 160, 60, 110, 50)
    Ridgewood = Hotel('Ridgewood', 5, 220, 150, 100, 40)
    client_type = entry.split(':')[0]
    reservation_days = re.findall(r'\((.*?)\)', entry.split(':')[1])  # Tratamento da entrada com regex
    prices_by_name = {}
    for hotel in Hotel.get_hotel().keys():
        prices_by_name[hotel] = locals()[hotel].get_total_price(client_type, reservation_days)
    same_price = []
    for hotel in prices_by_name.keys():
        if prices_by_name[hotel] == min(prices_by_name.values()):
            same_price.append(hotel)
    if len(same_price) == 1:
        cheapest_hotel = same_price[0]
    else:
        same_price_dict = {}  # Condição para mais de um hotel com o preço mais baixo
        for hotel in same_price:
            if hotel in Hotel.get_hotel().keys():
                same_price_dict[hotel] = Hotel.get_hotel()[hotel]
        cheapest_hotel = max(same_price_dict, key=same_price_dict.get)
    return cheapest_hotel
