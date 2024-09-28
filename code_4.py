import pandas as pd
df = pd.read_csv('./big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    # use query that focuses on both the year and country code
    query = f"(date == '{year}' and iso_a3 == '{country_code.upper()}')"
    sub_df = df.query(query)
    mean_price =sub_df['dollar_price'].mean()
    return round(mean_price, 2)


def get_big_mac_price_by_country(country_code):
    # use different query to focus on the country code
    queryc = f"(iso_a3 == '{country_code.upper()}')"
    sub_df = df.query(queryc)
    # get the mean of price 
    mean_price = sub_df['dollar_price'].mean()
    return round (mean_price,2)



def get_the_cheapest_big_mac_price_by_year(year):
    # make a query that checks the years by focusing on the date
    queryd = f"(date == '{year}')"
    sub_df = df.query(queryd)
    # locate the column, row, and index by using .loc to find the min index
    minimum = sub_df.loc[sub_df['dollar_price'].idxmin()]
    # locate the country name by using a separate variable and the minimum variable
    c_name = minimum['name']
    # locate the country code using a separate variable and the minimum variable
    code = minimum['iso_a3']
    # get the price using the minimum variable and using the dollar_price and round into 2 decimals
    price = round(minimum['dollar_price'],2)
    return f"{c_name}({code}): ${price}"

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    pass 