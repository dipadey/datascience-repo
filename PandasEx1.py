import pandas as pd
a=('aa',123,'2020-02-01','dd')
b=pd.Series(a,index=['Name','No','Date','Abbrv'])
print (b)
print ('Name:',b['Name'])
print (b[['Name','Abbrv']])

dict={'Name':'Rach','Age':30,'Salary':100000}
d=pd.Series(dict)
print (d)

dict1={'Name':['AA','BB','CC','DD'],
       'Desg':['SE','CS','SSE','CS'],
       'Salary':[60000,150000,100000,170000],
       'Level':[5,4,5,4]}

df1=pd.DataFrame(dict1,index=['E1','E2','E3','E4'])
print (df1)
df=pd.DataFrame(dict1,index=[x for x in range (1,5)])
print (df)

df['Company']='Xyz Pvt Ltd.'
print (df)

df=df.set_index(['Name'])
print (df)

print (df['Desg'])

print (df.iloc[1,1])
