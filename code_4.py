import pandas as pd
df = pd.read_csv('./big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    query = f"(date == '{year}' & iso_a3 == '{country_code.lower()}')"
    sub_df = df.query(query)
    mean_price =sub_df['dollar_price'].mean()
    return round(mean_price, 2)


def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    pass 