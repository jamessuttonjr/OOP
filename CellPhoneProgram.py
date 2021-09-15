

import CellPhoneClass as c


def main():
    phone = c.CellPhone("AT&T", "698flr", 600)
    phone.set_manufact("Verizon")
    print(phone.get_manufact())
    print(phone.get_model())
    print("$", phone.get_retail_price(), sep='')


main()
