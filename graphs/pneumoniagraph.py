#PNEUMONIA
import matplotlib.pyplot as p
p.title('PNEUMONIA(1990-2017)')
x=[1,2,3,4,5,6,7]
year=[1990,1995,2000,2005,2010,2015,2017]
deaths=[3.42,3.27,2.98,2074,2.62,2.58,2.56]
p.xlabel('year(1990-2017)')
p.ylabel('deaths*10^6in millions')
p.plot(year,deaths,color='black',label='deaths',linestyle='dashed')
p.legend()
p.show()

