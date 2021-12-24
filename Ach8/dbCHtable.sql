CREATE DATABASE dbClickHouse

CREATE TABLE dbClickHouse.table (TickTime DOUBLE, Speed DOUBLE, Day INT) 
ENGINE=Memory

SELECT TickTime, Day, Speed FROM dbClickHouse.table
WHERE (Day=1 and Speed > 8031238) or (Day=2 and Speed > 8325340)
ORDER BY Day Desc

#1    8.031238e+06
#2    8.325340e+06