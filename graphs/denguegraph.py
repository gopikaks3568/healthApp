#dengue
import matplotlib.pyplot as p
p.title("Dengue (2009-2017) ")
x=[1,2,3,4,5,6,7,8]
p.xlabel("2009-2017")
p.ylabel("cases")
year=[2009,2010,2011,2012,2013,2014,2015,2016,2017]
deaths=[165,110,160,259,174,256,240,250,300]
cases=[10956,15452,96000,52000,75965,36201,96520,11962,15003]
p.plot(year,cases,color='red',label='cases',linewidth='1')
p.plot(year,deaths,color='black',label='deaths',linewidth='2')
p.legend()
p.show()
