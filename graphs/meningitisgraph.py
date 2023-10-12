#MENINGITIS
import matplotlib.pyplot as p
p.title('MENINGITIS')
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
cases=[1.5,0.75,1,2,3,3.5,6,4,1.5,4.5,1,1.75,0.2,0.62,0.42]
deaths=[0.4,0.1,0.5,1.5,1.2,2,1.2,0.5,0.1,0.2,0.12,0.2,0.1,0.5,0.12]
p.ylabel('Number of confirmed cases')
p.plot(year,cases,color='red',label='cases',marker='.')
p.plot(year,deaths,color='black',label='deaths',marker='.')
p.legend()
p.show()
