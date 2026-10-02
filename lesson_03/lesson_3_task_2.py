from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79123456789"),
    Smartphone("Samsung", "Galaxy S21", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79345678901"),
    Smartphone("Google", "Pixel 6", "+79456789012"),
    Smartphone("Huawei", "P50", "+79567890123"),
]

for smartphone in catalog:
    print(
        f"{smartphone.brand} - {smartphone.model}. "
        f"{smartphone.phone_number}"
    )