class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (
            f"Отправление {self.track} из "
            f"{self.from_address.index}, {self.from_address.city}, "
            f"{self.from_address.street}, {self.from_address.house} - "
            f"{self.from_address.apartment} в "
            f"{self.to_address.index}, {self.to_address.city}, "
            f"{self.to_address.street}, {self.to_address.house} -"
            f"{self.to_address.apartment}. "
            f"Стоимость {self.cost} рублей."
        )