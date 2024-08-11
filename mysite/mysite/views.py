from json import JSONEncoder
from django.http import JsonResponse

from mysite import jalali

allDataFileQuery = "SELECT emp_no, recdate, term, nof_fish from datafile where recdate between '2024-05-21' and '2024-06-20'"
employeeShiftQuery = 'SELECT D{} from kara.dbo.empshift where emp_no={} and year={} and month={}'
freeOrPayQuery = 'select {} from kara.dbo.shifts where shift_no={}'
mealCodeQuery = "SELECT meal1 FROM MEALORDR where modate='{}' and term = {}"
mealPriceQuery = "SELECT top 1 price from MEALPRIC where meal_code={} and change_date<='{}' order by change_date desc"
mealEmpPriceQuery = "SELECT top 1 emp_price from MEALPRIC where meal_code={} and change_date<='{}' order by change_date desc"
empTypeCode =  "SELECT emp_type from kara.dbo.Employee where emp_no={}"
empTypeTitleQuery= "SELECT  title  from kara.dbo.EmpTypes where emptype_no={} "

def test(request):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(allDataFileQuery)
    allDataFile = cursor.fetchall()
    sum = 0
    for index in range(0, len(allDataFile)):
        year, month, day = jalali.Gregorian(allDataFile[index][1].strftime('%Y-%m-%d')).persian_tuple()
        employee_shift = cursor.execute(employeeShiftQuery.format(day, allDataFile[index][0], year, month))
        employee_shift = employee_shift.fetchall()
        if len(employee_shift) != 0:  # agar 0 bood ina doctoranb felanan
            freeOrPay = cursor.execute(
                freeOrPayQuery.format("term{}".format(allDataFile[index][2]), employee_shift[0][0]))
            freeOrPay = freeOrPay.fetchall()
            if len(freeOrPay) != 0:
                mealCode = cursor.execute(mealCodeQuery.format(allDataFile[index][1], allDataFile[index][2]))
                mealCode = mealCode.fetchall()
                mealPrice = cursor.execute(mealPriceQuery.format(mealCode[0][0], allDataFile[index][1]))
                mealPrice = mealPrice.fetchall()
                mealEmpPrice = cursor.execute(mealEmpPriceQuery.format(mealCode[0][0], allDataFile[index][1]))
                mealEmpPrice = mealEmpPrice.fetchall()
                if(len(mealPrice) == 0 or len(mealEmpPrice) == 0):
                    print(mealPriceQuery.format(mealCode[0][0], allDataFile[index][1]))
                # else:
                calculatedPrice = (mealEmpPrice[0][0] if freeOrPay[0][0] else mealPrice[0][0]) + (
                            (allDataFile[index][3] - 1) * mealPrice[0][0])
                meal_name = cursor.execute("SELECT title FROM meals where meal_code={}".format(mealCode[0][0]))
                meal_name = meal_name.fetchall()
                emp_name = cursor.execute(
                    "SELECT name,family,emp_type FROM kara.dbo.employee where emp_no={}".format(int(allDataFile[index][0])))
                emp_name = emp_name.fetchall()
                empTypeTitle = cursor.execute(empTypeTitleQuery.format(emp_name[0][2]))
                empTypeTitle = empTypeTitle.fetchall()
                if len(mealPrice) != 0:
                    a = 0
                    print("{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}".format(int(allDataFile[index][0]), emp_name[0][0] , emp_name[0][1], empTypeTitle[0][0],
                          year,month, day,
                          employee_shift[0][0],
                          allDataFile[index][2], meal_name[0][0],freeOrPay[0][0],allDataFile[index][3], int(calculatedPrice)))
                else:
                    sum += 1
                    # print(che_ghazaee_khorder_shode[0][0], shamsi_month, shamsi_day)
                    # print("SELECT top 1 {} from MEALPRIC where meal_code={} and change_date<'{}' order by change_date desc"
                    #     .format("emp_price" if mofi_or_poolaki[0][0] else "price",che_ghazaee_khorder_shode[0][0], allDataFile[0][1]))
    print(sum)
    return JsonResponse({'total': 0}, encoder=JSONEncoder)
