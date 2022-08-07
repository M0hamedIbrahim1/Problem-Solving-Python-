/*
  link   : https://www.hackerrank.com/challenges/weather-observation-station-8/problem
  author : Mohamed Ibrahim
*/

select distinct city from station where right(city, 1) in ('a','e','i','o','u') and left(city, 1) in ('a','e','i','o','u');
