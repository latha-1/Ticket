#Refer : Refer https://www.hostinger.in/tutorials/how-to-install-mysql-on-centos-7

1: sudo wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
2: sudo rpm -Uvh mysql80-community-release-el7-3.noarch.rpm
3: sudo yum install mysql-server
4: sudo systemctl start mysqld
5: sudo systemctl status mysqld
6: sudo mysql_secure_installation
7: mysql -u root -p

#Database Creation Syntax:
Create <NewDataBaseName>;

#Example:
Create Production;

#How to enter Database Syntax:
use <DataBaseName>;

#Example:
use Production;

#Table Creation Syntax:
CREATE TABLE <new_table_name> (name VARCHAR(20), owner VARCHAR(20),
species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);

#Example:
CREATE TABLE StudentDetails (name VARCHAR(20), owner VARCHAR(20),
species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);



#Yes Yes No No yes

New Password: 
Re Enter New Password: 


Server IP: lohalhost
User: root
Password: Simba@26526

#To Fetch All the records from table
#Select * From StudentDetails;

#Condition wise To Fetch The records
#Select * From StudentDetails Where name = 'anjan';

#Update * From StudentDetails Set sex = 'F' Where name = 'divya';