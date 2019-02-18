def discount(new_cust, loyalty_card, coupon):
    discount = 0

    if new_cust and loyalty_card:
        return None

    if new_cust:
        discount += 15
    if coupon:
        discount = 20
    if loyalty_card:
        discount += 10

    return discount