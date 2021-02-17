# SQL

## SQL Commands

### 0 - Most Importand Commands

- SELECT - extracts data from a database
- UPDATE - updates data in a database
- DELETE - deletes data from a database
- INSERT INTO - inserts new data into a database
- CREATE DATABASE - creates a new database
- ALTER DATABASE - modifies a database
- CREATE TABLE - creates a new table
- ALTER TABLE - modifies a table
- DROP TABLE - deletes a table
- CREATE INDEX - creates an index (search key)
- DROP INDEX - deletes an index

### 0.1 - Keep in Mind

- Note: Most of the SQL database programs also have their own proprietary extensions in addition to the SQL standard!
- Note: SQL keywords are NOT case sensitive: select is the same as SELECT


### 1 - *SELECT* COMMAND

- The SELECT statement is used to select data from a database.

```SQL
SELECT column1, column2, ...
FROM table_name;
```

#### 1.1 - *SELECT DISTINCT*

The SELECT DISTINCT statement is used to return only distinct (different) values.

```SQL
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

```SQL
SELECT COUNT(DISTINCT column1) FROM table_name;
```

#### 2 - *WHERE*

The WHERE clause is used to filter records.

```SQL
SELECT column FROM table_name WHERE condition;
```

**Note**: The WHERE clause is not only used in SELECT statement, it is also used in UPDATE, DELETE statement, etc.!

#### 3 - *SQL AND, OR and NOT Operators*

#### 4 - *ORDER BY*

The ORDER BY keyword is used to sort the result-set in ascending or descending order.

```SQL
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

#### 5 - *INSERT INTO*

The INSERT INTO statement is used to insert new records in a table.

```SQL
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

```SQL
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

#### 6 - *NULL Values*

A field with a NULL value is a field with no value.

```SQL
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```

```SQL
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```

#### 7 - *UPDATE*

The UPDATE statement is used to modify the existing records in a table.

```SQL
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

**Note**: Be careful when updating records in a table! Notice the WHERE clause in the UPDATE statement. The WHERE clause specifies which record(s) that should be updated. If you omit the WHERE clause, all records in the table will be updated!

#### 8 - *DELETE*

The DELETE statement is used to delete existing records in a table.

```SQL
DELETE FROM table_name WHERE condition;
```

Note: Be careful when deleting records in a table! Notice the WHERE clause in the DELETE statement. The WHERE clause specifies which record(s) should be deleted. If you omit the WHERE clause, all records in the table will be deleted!

#### 9 - *SELECT TOP*


#### 10 - *MIN() and MAX() Functions*

```SQL
SELECT MIN(column_name)
FROM table_name
WHERE condition;
```

```SQL
SELECT MAX(column_name)
FROM table_name
WHERE condition;
```

#### 11 - *AVG() , COUNT() and SUM() Functions*

```SQL
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

```SQL
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```

```SQL
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```

#### 12 - *LIKE Operator*

The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.
There are two wildcards often used in conjunction with the LIKE operator:

% - The percent sign represents zero, one, or multiple characters
_ - The underscore represents a single character

```SQL
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
```

LIKE Operator|Description|
| -------------- |:------------------:|
WHERE CustomerName LIKE 'a%'| Finds any values that start with "a"|
WHERE CustomerName LIKE '%a' | Finds any values that end with "a"|
WHERE CustomerName LIKE '%or%'| Finds any values that have "or" in any position|
WHERE CustomerName LIKE '_r%'|Finds any values that have "r" in the second position|
WHERE CustomerName LIKE 'a_%'|Finds any values that start with "a" and are at least 2 characters in length|
WHERE CustomerName LIKE 'a__%'|Finds any values that start with "a" and are at least 3 characters in length|
WHERE ContactName LIKE 'a%o'|Finds any values that start with "a" and ends with "o"|

#### 13 -*IN Operator*

The IN operator allows you to specify multiple values in a WHERE clause.
The IN operator is a shorthand for multiple OR conditions.

```SQL
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

```SQL
SELECT column_name(s)
FROM table_name
WHERE column_name IN (SELECT STATEMENT);
```




## Source

- <https://www.w3schools.com/sql/default.asp>
