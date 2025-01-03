use dbtest
create table tblEmployee(
    EmployeeNumber tinyint not null identity (1,1),
    EmployeeFirstName nvarchar(20) not null,
    EmployeeMiddleName nvarchar(20),
    EmployeeLastName nvarchar(20) not null,
    EmployeeGovernmentID varchar(10), --bigint is 8 bytes
    DateOfBirth date not null,
    primary key (EmployeeNumber)
)

select * from tblEmployee



insert into _9_tblEmployee (employeefirstname, employeemiddlename,employeelastname,
 employeegovernmentid, dateofbirth, department)
values (
'Jane','','Zwilling','AB123456G''1/1/1999','Litigation'
)

select * from _9_tblEmployee


alter table _9_tblEmployee alter column Department nvarchar(30)
exec sp_help '_9_tblEmployee'