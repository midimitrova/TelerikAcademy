total_text = int(input())
total_minutes = int(input())

additional_text = total_text - 20
additional_minutes = total_minutes - 60

price_additional_text = additional_text * 0.06
price_additional_minutes = additional_minutes * 0.10

add_tax = price_additional_text * 20/100 + price_additional_minutes * 20/100
total_price = 12 + price_additional_text + price_additional_minutes + add_tax


if total_text <= 20 and total_minutes <= 60:
    print(f'{0} additional messages for {0:.2f} levas')
    print(f'{0} additional minutes for {0:.2f} levas')
    print(f'{0:.2f} additional taxes')
    print(f'{12:.2f} total bill')
elif total_text <= 20 or total_minutes <= 60:
    if total_text <= 20 and total_minutes > 60:
        print(f'{0} additional messages for {0:.2f} levas')
        print(f'{additional_minutes} additional minutes for {price_additional_minutes:.2f} levas')
        print(f'{(price_additional_minutes * 20/100):.2f} additional taxes')
        print(f'{(12 + price_additional_minutes * 20/100 + price_additional_minutes):.2f} total bill')
    elif total_text > 20 and total_minutes <= 60:
        print(f'{additional_text} additional messages for {price_additional_text:.2f} levas')
        print(f'{0} additional minutes for {0:.2f} levas')
        print(f'{(price_additional_text * 20/100):.2f} additional taxes')
        print(f'{(12 + price_additional_text * 20/100 + price_additional_text):.2f} total bill')
else:
    print(f'{additional_text} additional messages for {price_additional_text:.2f} levas')
    print(f'{additional_minutes} additional minutes for {price_additional_minutes:.2f} levas')
    print(f'{add_tax:.2f} additional taxes')
    print(f'{total_price:.2f} total bill')
