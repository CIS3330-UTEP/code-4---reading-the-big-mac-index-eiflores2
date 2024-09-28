import pandas as pd
df = pd.read_csv('./big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    # use query that focuses on the year
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    sub_df = df.query(query)
    # use query that focuses on the country code
    query_c = f"(iso_a3 == '{country_code.upper()}')"
    cc = sub_df.query(query_c)
    # get the mean and the price from the column
    mean_price =cc['dollar_price'].mean()
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
    queryd = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
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
    # most of the code is above in the min, just copy it and change the values from min to max
    queryd = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    sub_df = df.query(queryd)
    # locate the column, row, and index by using .loc to find the max index
    maxx = sub_df.loc[sub_df['dollar_price'].idxmax()]
    # locate the country name by using a separate variable and the maxx variable
    c_name = maxx['name']
    # locate the country code using a separate variable and the maxx variable
    code = maxx['iso_a3']
    # get the price using the maxx variable and using the dollar_price and round into 2 decimals
    price = round(maxx['dollar_price'],2)
    return f"{c_name}({code}): ${price}"

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2012,'jpn')
    print(result_a)
    result_b = get_big_mac_price_by_country('mex')
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2003)
    print(result_d)