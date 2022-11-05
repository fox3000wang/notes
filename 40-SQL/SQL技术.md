# SQL

## 关系型数据库模型(RDBMS)

## SQL99 语句分类

| 类型     | 简介                    | 命令举例                    |
| -------- | ----------------------- | --------------------------- |
| 连接语句 | 开始和结束一个客户连接  | connect,disconnect          |
| 控制语句 | 控制一组 SQL 语句的执行 | call, return                |
| 数据语句 | 直接操作数据库          | select,insert,update,delete |
| 模式语句 | 更改表结构              | alter,create，drop          |
| 事物语句 | 设置一个事物开始和结束  | commit, rollback            |

## mysql 数据类型

### 数值类型

| 类型           | 大小            | 用途     |
| -------------- | --------------- | -------- |
| TINYINT        | 1 Bytes         | 小整数值 |
| SMALLINT       | 2 Bytes         | 大整数值 |
| MEDIUMINT      | 3 Bytes         | 大整数值 |
| INT 或 INTEGER | 4 Bytes         | 大整数值 |
| DECIMAL        | 对 DECIMAL(M,D) | 小数值   |

### 日期和时间类型

| 类型      | 大小( bytes) | 范围                                         | 格式                | 用途                     |
| --------- | ------------ | -------------------------------------------- | ------------------- | ------------------------ |
| DATE      | 3            | 1000-01-01/9999-12-31                        | YYYY-MM-DD          | 日期值                   |
| TIME      | 3            | '-838:59:59'/'838:59:59'                     | HH:MM:SS            | 时间值或持续时间         |
| YEAR      | 1            | 1901/2155                                    | YYYY                | 年份值                   |
| DATETIME  | 8            | '1000-01-01 00:00:00'到'9999-12-31 23:59:59' | YYYY-MM-DD hh:mm:ss | 混合日期和时间值         |
| TIMESTAMP | 4            | '1970-01-01 00:00:01'到'2038-01-19 03:14:07' | YYYY-MM-DD hh:mm:ss | 混合日期和时间值，时间戳 |

### 字符串类型

| 类型       | 大小                  | 用途                            |
| ---------- | --------------------- | ------------------------------- |
| CHAR       | 0-255 bytes           | 定长字符串                      |
| VARCHAR    | 0-65535 bytes         | 变长字符串                      |
| TINYBLOB   | 0-255 bytes           | 不超过 255 个字符的二进制字符串 |
| TINYTEXT   | 0-255 bytes           | 短文本字符串                    |
| BLOB       | 0-65 535 bytes        | 二进制形式的长文本数据          |
| TEXT       | 0-65 535 bytes        | 长文本数据                      |
| MEDIUMBLOB | 0-16 777 215 bytes    | 二进制形式的中等长度文本数据    |
| MEDIUMTEXT | 0-16 777 215 bytes    | 中等长度文本数据                |
| LONGBLOB   | 0-4 294 967 295 bytes | 二进制形式的极大文本数据        |
| LONGTEXT   | 0-4 294 967 295 bytes | 极大文本数据                    |

## 数据语句(CRUD)

### insert

```sql
  INSERT INTO user_table (name, age) VALUAS ("小王", 5);
```

### delete

```sql
  DELETE FROM user_table WHERE name = "小王";
```

### update

```sql
  UPDATE user_table SET age = 6 WHERE name = "小王";
```

### select

```sql
  SELECT age, user_name FROM table_name;
```

### where 条件子语句

| 简写形式          | 例子                         | 简介                                   |
| ----------------- | ---------------------------- | -------------------------------------- |
| 布尔检验          | WHERE id = '314'             | 用运算符 > < <> LIKE ...               |
| 多个搜索          | WHERE id = '314' AND f = '0' | AND 和 OR 连接                         |
| NULL 检验         | WHERE id IS NOT NULL         | IS NULL                                |
| JOIN 检验         | WHERE t1.id = t2.u_id        |                                        |
| LIKE 检验         | WHERE phone LIKE '130%'      | 用于模糊查询                           |
| EXIST 存在性检验  | WHERE EXIST (SELECT ...)     | 与子查询一起用, 子查询只是进行布尔检验 |
| BETWEEN 范围检验  | WHERE age BETWEEN 3 AND 5    | 和 age > 3 AND age < 5 相似            |
| IN 范围检验       | WHERE age IN (SELECT ...)    |                                        |
| SOME\ALL 范围检验 | WHERE age > ANY (SELECT ...) |                                        |

### ORDER BY 子句

默认排序顺序是升序的 ASC, 降序是 DESC

```sql
SELECT * FROM employees ORDER BY first_name, last_name;
```

### TOP 语法

## 函数

## 参考

https://www.cainiaojc.com/sql/sql-tutorial.html
