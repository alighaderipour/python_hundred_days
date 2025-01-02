/*
char  > works in ASCII range  1 byte
varchar > works in ASCII range 1 byte
nchar > works in UNICODE range 2 bytes
nvarchar > > works in UNICODE range 2 bytes


 */
-- if you want to use a fixed length like national code better use char , if you want to store something like names its better to use varchar
-- if you use char(10) regardless of how many character you use it will cost you 10 bytes
-- if you use varchar(10) maximum space that will be used is 20 bytes , for example 'ali' will be 3*2 = 6 bytes
 declare  @my_var nchar(9)
 set @my_var = 'Johnson'
 select @my_var as name
 select len(@my_var) as len
 select DATALENGTH(@my_var) as 'size in bytes'

-- there are some built-in string function in sql like "replace", "rtrim","ltrim" etc
-- https://learn.microsoft.com/en-us/sql/t-sql/functions/string-functions-transact-sql?view=sql-server-ver16
-- just google string function sql

