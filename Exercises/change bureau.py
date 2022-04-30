amount_bitcoins = int(input())
amount_uans = float(input())
comission = float(input())

fiat_info = {
    "bitcoin": 1168,
    "uans": 0.15,
    "dollars": 1.76,
    "euro": 1.95
}

calculation = (amount_bitcoins * fiat_info["bitcoin"]) + ((amount_uans * fiat_info["uans"]) * fiat_info["dollars"])
leva_to_euro = calculation / fiat_info["euro"]
comission = (leva_to_euro * comission) / 100
total = leva_to_euro - comission

print(f"{total:.2f}")