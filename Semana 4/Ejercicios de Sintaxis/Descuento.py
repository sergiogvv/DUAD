product_price = float(input("Ingrese precio del producto: "))
if product_price < 100:
    discount = 0.02
elif product_price >= 100:
    discount = 0.1

final_price = product_price * (1 - discount)
print(f"El precio final del producto es: {final_price:.2f}")