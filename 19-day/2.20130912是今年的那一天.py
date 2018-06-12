def is_leap_year(year):
	if year%400==0 or (year%4==0 and year%100!=0):
		return 1
	else:
		return 0

def month_turn_day(year,month,day):
	day_sum = 0
	month31 = [1,3,5,7,8,10,12]
	month30 = [4,6,9,11]
	for x in range (1,month):
		if x in month31:
			day_sum += 31
		elif x in month30:
			day_sum += 30
		elif is_leap_year(year) and x==2:
			day_sum += 29
		elif x == 2:
			day_sum += 28
	day_sum += day
	print('%s是今年的第%d天'%(time,day_sum))

def get_y_m_d(time):
	year = int(time[0:4])
	month = int(time[4:6])
	day = int(time[6:8])
	month_turn_day(year,month,day)
time = '19981118'
get_y_m_d(time)