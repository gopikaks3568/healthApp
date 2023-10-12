#cholera#true values 
import matplotlib.pyplot as p
p.title('Cholera')
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,]
year=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
cases=[3056,4059,5019,8129,15325,2064,10592,7851,6215,4591,4495,3265,4529,22848,19562,18532,13265,1495]
deaths=[485,3156,4512,6254,9005,295,456,8054,542,566,946,2054,2015,15219,10491,12059,1054,652]
p.xlabel('cases')
p.ylabel('deaths')
p.plot(year,cases,color='red',label='cases',linestyle='dashed')
p.plot(year,deaths,color='black',label='deaths',linestyle='dashed')
p.legend()
p.show()
