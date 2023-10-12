#CORONA 
import matplotlib.pyplot as p
p.title('CORONA(SEPTEMBER-OCTOBER 2020 )')
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
cases=[26002010,26290668,2688946,27410142,27864960,2845996,30168178,30809297,31368494,31884863,30018699,33409634,33255665,35211180,35211452,363900589]
deaths=[874947,881394,887395,898231,902472,910771,916996,923013,928798,933903,942166,94923,1259252,1918299,1029697,2155307]
p.xlabel('cases')
p.ylabel('deaths')
p.plot(x,cases,color='red',label='cases',marker='.')
p.plot(x,deaths,color='black',label='deaths',marker='.')
p.legend()
p.show()
