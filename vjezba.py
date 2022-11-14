
import sqlite3
conn = sqlite3.connect('Sensors.db')
c = conn.cursor()

c.execute("SELECT Lines, Value, Action FROM Temperature WHERE Value = 22")
fetch = c.fetchall()
print(fetch)
print(type(fetch))
print("****")
for row in fetch:
    print(row)
    #print(f"{row[0]}  {row[1]}°C\t {row[2]}")

print("######")
c.execute("SELECT Lines, Value, Action FROM Temperature WHERE Value = 22")
fetch1 = c.fetchone()
print(fetch1)
print(type(fetch1))
print(f"{fetch1[0]}  {fetch1[1]}°C\t {fetch1[2]}")
conn.close()
