-- 코드를 입력하세요
SELECT count(*) AS USERS
FROM USER_INFO
WHERE AGE >= 20 and AGE <=29 AND Year(JOINED) = 2021
