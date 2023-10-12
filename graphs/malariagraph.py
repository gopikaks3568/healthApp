#MALARIA #completed 
import matplotlib.pyplot as p
p.title('MALARIA')
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
year=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
cases=[3.2,2.9,3.1,3.4,4.0,4.0,4.1,2.5,2.5,3.0,3.2,2.0,12.1,7.5,8.5]
deaths=[10.0,2.8,4.6,4.5,3.0,3.1,5.2,7.5,6.8,5.8,6.4,6.4,5.1,4.3,4.6,]
p.xlabel('year(2000-2014)')
p.ylabel('Cases *10^6 (in millions )  , Deaths *10^3(in thousands)')
p.plot(year,cases,color='red',label='cases',marker='.')
p.plot(year,deaths,color='black',label='deaths',marker='.')
p.legend()
p.show()
