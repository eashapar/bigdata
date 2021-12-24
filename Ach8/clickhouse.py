import tarantool
import pandas as pd
import pandahouse as ph

# подключаемся к тарантулу
connection = tarantool.connect("localhost", 3301, user='admin', password='pa$$w0rd')
# сохраняем данные в переменную
tester = connection.space('frommqtt')
data = tester.select()
# панда-датафрейм
df = pd.DataFrame(data, columns=['Day', 'TickTime', 'Speed'])
print (df)
# коннектимся к кликхаусу
connection = dict(database='dbClickHouse', user='default')
# переносим данные в него
ph.to_clickhouse(df, 'table', connection=connection, index=False)