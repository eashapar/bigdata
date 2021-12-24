CREATE DATABASE dbClickHouse

CREATE TABLE dbClickHouse.table (TickTime DOUBLE, Speed DOUBLE, Day INT) 
ENGINE=Memory

SELECT TickTime, Day, Speed FROM dbClickHouse.table
WHERE (Day=1 and Speed > 8056629) or (Day=2 and Speed > 8335122) or (Day=3 and Speed > 7338770)
ORDER BY Day Desc

#1    8.056629e+06
#2    8.335122e+06
#7    7.338770e+06