from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Тверская", "1", "10")
from_address = Address("654321", "Санкт-Петербург", "Невский", "2", "20")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=250,
    track="TRACK123456",
)

print(mailing)