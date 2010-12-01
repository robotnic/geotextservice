
def dbconnect
require 'rubygems'
require "mysql"

host="localhost"
username="dm101507"
password="gairdixnu" 
dbname = "dm101507"

dbh=Mysql.init


dbh.options(Mysql::SET_CHARSET_NAME, "utf8")
dbh.real_connect(host,username,password,dbname)
dbh.query("SET NAMES utf8")
return dbh
end
