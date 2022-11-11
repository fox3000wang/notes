# MYSQL 运维

## 安装

```shell
sudo apt install mysql-server
sudo apt install mysql
```

## 启动

```shell
sudo service mysql start

不然会报错：
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
```

## 初次登陆

```shell
# I had to use "sudo" since it was a new installation
sudo mysql -u root

不然会报:
ERROR 1698 (28000): Access denied for user 'root'@'localhost'
```

## root 用户有点特别，需要重新建一个类 root 用户(可以不做)

```mysql
mysql> USE mysql;
mysql> SELECT User, Host, plugin FROM mysql.user;

mysql> CREATE USER 'ubuntu'@'localhost' IDENTIFIED BY 'YOUR_PASSWD';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'ubuntu'@'localhost';
mysql> UPDATE user SET plugin='auth_socket' WHERE User='YOUR_SYSTEM_USER';
mysql> FLUSH PRIVILEGES;
mysql> exit;

sudo service mysql restart
mysql -uubuntu #直接登陆

+------------------+-----------+-----------------------+
| User             | Host      | plugin                |
+------------------+-----------+-----------------------+
| debian-sys-maint | localhost | mysql_native_password |
| mysql.infoschema | localhost | caching_sha2_password |
| mysql.session    | localhost | mysql_native_password |
| mysql.sys        | localhost | mysql_native_password |
| root             | localhost | auth_socket           |
| ubuntu           | localhost | auth_socket           |
+------------------+-----------+-----------------------+
```

## 创建普通用户

```shell
-- 创建一个可以远程连接但是权限小一点的用户
mysql> CREATE USER 'user'@'%' IDENTIFIED BY 'useruser';
mysql> GRANT ALL ON *.* TO 'user'@'%';
mysql> FLUSH PRIVILEGES;
mysql> exit;

sudo service mysql restart
```

## 配置 mysql 可以支持远程访问

sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

```shell
bind-address            = 127.0.0.1
mysqlx-bind-address     = 127.0.0.1
改成：
bind-address            = 0.0.0.0
mysqlx-bind-address     = 0.0.0.0
```

sudo service mysql restart
