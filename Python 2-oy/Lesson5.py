currency_data = [
    {
        "title": "BAA dirham",
        "code": "AED",
        "cb_price": "3435.74",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Australian dollar",
        "code": "AUD",
        "cb_price": "8345.49",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Canadian dollar",
        "code": "CAD",
        "cb_price": "9197.46",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Swiss franc",
        "code": "CHF",
        "cb_price": "13915.35",
        "nbu_buy_price": "13600.00",
        "nbu_cell_price": "14400.00",
        "date": "31.05.2024"
    },
    {
        "title": "Chinese yuan",
        "code": "CNY",
        "cb_price": "1743.60",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Danish krone",
        "code": "DKK",
        "cb_price": "1829.31",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Egyptian pound",
        "code": "EGP",
        "cb_price": "266.92",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Euro",
        "code": "EUR",
        "cb_price": "13645.82",
        "nbu_buy_price": "13450.00",
        "nbu_cell_price": "13650.00",
        "date": "31.05.2024"
    },
    {
        "title": "British pound sterling",
        "code": "GBP",
        "cb_price": "16043.59",
        "nbu_buy_price": "15800.00",
        "nbu_cell_price": "16500.00",
        "date": "31.05.2024"
    },
    {
        "title": "Icelandic króna",
        "code": "ISK",
        "cb_price": "91.52",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Japanese yen",
        "code": "JPY",
        "cb_price": "80.41",
        "nbu_buy_price": "70.00",
        "nbu_cell_price": "90.00",
        "date": "31.05.2024"
    },
    {
        "title": "South Korean won",
        "code": "KRW",
        "cb_price": "9.17",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Kuwaiti dinar",
        "code": "KWD",
        "cb_price": "41133.74",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Kazakhstani tenge",
        "code": "KZT",
        "cb_price": "28.35",
        "nbu_buy_price": "15.00",
        "nbu_cell_price": "30.00",
        "date": "31.05.2024"
    },
    {
        "title": "Lebanese pound",
        "code": "LBP",
        "cb_price": "0.14",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Malaysian ringgit",
        "code": "MYR",
        "cb_price": "2682.79",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Norwegian krone",
        "code": "NOK",
        "cb_price": "1194.96",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Polish złoty",
        "code": "PLN",
        "cb_price": "3182.65",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Russian ruble",
        "code": "RUB",
        "cb_price": "140.36",
        "nbu_buy_price": "100.00",
        "nbu_cell_price": "150.00",
        "date": "31.05.2024"
    },
    {
        "title": "Swedish krona",
        "code": "SEK",
        "cb_price": "1186.61",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Singapore dollar",
        "code": "SGD",
        "cb_price": "9338.34",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Turkish lira",
        "code": "TRY",
        "cb_price": "390.59",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Ukrainian hryvnia",
        "code": "UAH",
        "cb_price": "311.64",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "US dollar",
        "code": "USD",
        "cb_price": "12619.83",
        "nbu_buy_price": "12580.00",
        "nbu_cell_price": "12660.00",
        "date": "31.05.2024"
    }
]

def exchange_currency():
    soum = int(input("Enter your money in soum: "))
    code = input("Enter the code of the currency: ").upper()

    for currency in currency_data:
        if currency['code'] == code:
            result = soum / float(currency['cb_price'])
            print(f"Your money in {currency['code']} = {result}")
            return show_menu()
        
    print("Wrong code!")
    return exchange_currency()


def find_currency():
    code = input("Enter the code of the currency: ").upper()

    for currency in currency_data:
        if currency['code'] == code:
            print(f"1 {currency['code']} is {currency['cb_price']} soum")
            return show_menu()
        
    print("Wrong code!")
    return find_currency()


def search_by_title():
    title = input("Enter the title of the currency: ").lower()

    for currency in currency_data:
        if title in currency['title'].lower():
            print(f"{currency['code']} \t {currency['cb_price']} \t {currency['title']}")
    return show_menu()


def show_menu():
    text = """
    1. Exchange currency
    2. Find currency in soum
    3. FromTo exchange
    4. Search by title
    5. Exit
    """
    print(text)

    user_input = int(input("Choose from the menu: "))
    if user_input == 1:
        exchange_currency()
    elif user_input == 2:
        find_currency()
    elif user_input == 3:
        print("FromTo exchange functionality not implemented yet.")
        return show_menu()
    elif user_input == 4:
        search_by_title()
    else:
        return print("Goodbye!!!")

if __name__ == '__main__':
    show_menu()