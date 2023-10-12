#TB
import matplotlib.pyplot as p
p.title('TUBERCULOSIS')
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,]
year=[1990,1992,1994,1996,1998,2000,2002,2004,2006,2008,2010,2012,2014,2016,2018]
cases=[23596,27593,24965,21456,18865,16342,13965,11394,13561,15632,11964,12845,11964,13952,9093]
deaths=[15364,19631,16954,18956,14525,12654,10961,9032,7315,14926,912,962,9215,1100,4521,]
p.xlabel('Number of cases')
p.ylabel('deaths')
p.plot(year,cases,color='red',label='cases',marker='.')
p.plot(year,deaths,color='black',label='deaths',marker='.')
p.legend()
p.show()
