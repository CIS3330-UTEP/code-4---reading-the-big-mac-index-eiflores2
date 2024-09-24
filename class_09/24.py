import pandas as pd

df = pd.read_csv('./big-mac-full-index.csv')

print(df)

country_code = "RUS"

query = f"(iso_a3 == '{country_code}')"

sub_df = df.query(query)
print(len(sub_df))
print(sub_df)

print(sub_df.loc[21])
print("\n")
print(sub_df.iloc[21])

print(sub_df['dollar_price'].mean())


new_query = f"date > '2012-01-01' and date < '2012-12-31'"

new_date_df = df.query(new_query)
print(new_date_df)
