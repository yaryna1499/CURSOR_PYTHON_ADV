-- 1. Таблиця Employees. Отримати список з інформацією про всіх співробітників
SELECT * FROM EMPLOYEES;

-- 2. Таблиця Employees. Отримати список всіх співробітників з ім'ям 'David'
SELECT * FROM EMPLOYEES WHERE FIRST_NAME LIKE 'David';


-- 3.Таблиця Employees. Отримати список всіх співробітників з 20го і з 30го відділу (department_id)
SELECT EMPLOYEES.FIRST_NAME, EMPLOYEES.LAST_NAME, DEPARTMENTS.DEPARTMENT_ID FROM EMPLOYEES 
INNER JOIN DEPARTMENTS ON EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID
WHERE DEPARTMENTS.DEPARTMENT_ID = 20 OR DEPARTMENTS.DEPARTMENT_ID = 30;


-- 4.Таблиця Employees. Отримати список всіх співробітників з 50го і з 80го відділу 
-- (department_id) у яких є бонус (значення в колонці commission_pct не порожнє)
SELECT EMPLOYEES.FIRST_NAME, EMPLOYEES.LAST_NAME, DEPARTMENTS.DEPARTMENT_ID FROM EMPLOYEES 
INNER JOIN DEPARTMENTS ON EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID
WHERE DEPARTMENTS.DEPARTMENT_ID = 20 OR DEPARTMENTS.DEPARTMENT_ID = 30 AND COMISSION_PCT IS NOT NULL OR COMISSION_PCT <> 0;


-- Таблиця Employees. Отримати список всіх співробітників які прийшли на роботу в перший день місяця (будь-якого)
SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEES
WHERE SUBSTRING(CAST(HIRE_DATE AS char), 6, 2) LIKE '01';


-- Таблиця Employees. Отримати список всіх співробітників які прийшли на роботу в 2008ом році
SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEES
WHERE SUBSTRING(CAST(HIRE_DATE AS char), 1, 4) LIKE '2008';

-- Таблиця DUAL. Показати завтрашню дату в форматі: Tomorrow is Second day of January
SELECT CONCAT('Tomorrow is the ', DATE_FORMAT(DATE_ADD(NOW(), INTERVAL 1 DAY),'%D day of %M')) as tomorrow_date
FROM DUAL;
 
 
 -- Таблиця Employees. Отримати список всіх співробітників і дату приходу на роботу кожного в форматі: 21st of June, 2007
 SELECT FIRST_NAME, LAST_NAME, DATE_FORMAT(HIRE_DATE,'%D day of %M, %Y')
 FROM EMPLOYEES;
 
 
 -- Таблиця Employees. Отримати список працівників зі збільшеними зарплатами на 20%. Зарплату показати зі знаком долара
 SELECT FIRST_NAME, LAST_NAME, concat(SALARY,'$') as salary
 FROM EMPLOYEES
 WHERE COMISSION_PCT = 20;
 
 -- Таблиця Employees. Отримати список всіх     співробітників які пришили на роботу в лютому 2007го року.
SELECT FIRST_NAME, LAST_NAME, HIRE_DATE
FROM EMPLOYEES
WHERE REPLACE(CAST(HIRE_DATE AS char), '-', '') like '200702%';


-- Таблиця DUAL. Вивезти актуальну дату, + секунда, + хвилина, + годину, + день, + місяць, + рік
SELECT NOW() FROM DUAL;

-- Таблиця Employees. Отримати список всіх співробітників з повними зарплатами (salary + commission_pct (%)) в форматі: $ 24,000.00
SELECT FIRST_NAME, LAST_NAME, concat(SALARY*(1+COMISSION_PCT/100),'$') as full_salary
FROM EMPLOYEES;

-- Таблиця Employees. Отримати список всіх співробітників і інформацію про наявність бонусів до зарплати (Yes / No)
SELECT FIRST_NAME, LAST_NAME, 
(case WHEN COMISSION_PCT IS NOT NULL then 'Yes' else 'No' end)
FROM EMPLOYEES;

