from sqlalchemy import create_engine
from sqlalchemy import text
import pandas

data_dict = {
    "students": ["Robert", "Tehera", "Tiffany"],
    "scores": [95, 92, 88],
    "Majors": ["CS", "CE", "SM"],
    "gender": ["M", "F", "F"]
}
print(data_dict)
print()
data = pandas.DataFrame(data_dict)
print(data)
print("=============")
print()

# cnt = 0
# for row in data:
#     print(pandas.DataFrame.loc[cnt, cnt + 1])
#     cnt += 1

# Create CSV
data.to_csv("scores.csv")

# ===================== #
#   Database Stuff      #
# ===================== #

# engine = create_engine('sqlite://', echo=False)
# df = pandas.DataFrame({'name' :['Robert', 'Tehera', 'Michael']})
# print(df)
# df.to_sql(name='users', con=engine)
#
# with engine.connect() as conn:
#     conn.execute(text("SELECT * FROM users")).fetchall()

# original_df = pandas.DataFrame({"foo": range(5), "bar": range(5,10)})
# print(original_df)
# original_df.to_pickle("dummy.pkl")
# print()
# unpickled_df = pandas.read_pickle("dummy.pkl")
# print(unpickled_df)