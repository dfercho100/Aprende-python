def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number."
    if not isinstance(discount, (int, float)):
        return "The discount should be a number."
    if price <= 0:
        return "The price should be greater than 0."
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100."
    discount_amount = price * (discount / 100)
    # si apply_discount(100, 20) se llama, el descuento_amount se calculará como 100 * (20 / 100) = 20.0. 
    # Luego, el precio final se calculará restando el descuento_amount del precio original: 100 - 20.0 = 80.0.
    #  Por lo tanto, el resultado de apply_discount(100, 20) será 80.0.
    #----------------------------
    # si apply_discount(200,50) se llama, el descuento_amount se calculará como 200 * (50 / 100) = 100.0. 
    # Luego, el precio final se calculará restando el descuento_amount del precio original: 200 - 100.0 = 100.0.
    #----------------------------
    #si apply_discount(74.5,20.0) se llama, el descuento_amount se calculará como 74.5 * (20 / 100) = 14.9. 
    # Luego, el precio final se calculará restando el descuento_amount del precio original: 74.5 - 14.9 = 59.6.
    #  Por lo tanto, el resultado de apply_discount(74.5,20.0) será 59.6.
    final_price = price - discount_amount
    return final_price
print(apply_discount(100, 20)) # 80.0
print(apply_discount(200, 50)) # 100.0
print(apply_discount(74.5, 20.0)) # 59.6