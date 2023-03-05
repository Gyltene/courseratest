from flask import Flask,render_template,request,redirect
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
import datetime


app=Flask(__name__,template_folder='./Templates',static_url_path='')


@app.route('/',methods=['GET','POST'])
def Shitja():
     return  render_template('Covid.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    data=pd.read_csv('owid-covid-data.csv',index_col=2)
    data['date']=data['date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%d-%m-%Y') if x != "" else "")
    data2=data[['date','new_cases','new_deaths','total_deaths','new_tests','new_vaccinations','people_vaccinated','people_fully_vaccinated','population']]
    data2.rename(columns={'new_cases':'Raste e Reja','new_deaths':'Te Vdekur','new_tests':'Te Testuar','population':'Numri i Popullesise','people_vaccinated':'Te vaksionuar me nje doze',
    'people_fully_vaccinated':'Te vaksionuar me dy doza','total_deaths':'Numri i pergjitheshem i vdekjeve deri me daten e caktuar:'},inplace=True)
   
    Numri1=request.form['Numri1']
    Numri2=request.form['Numri2']
    data2.index.name='Lokacioni'
    data3=(data2[data2.index==Numri1]) 
    data4=(data3[data3['date']==Numri2])
    
    
   
    data5=(data4[['Raste e Reja']])

    data5=data5.astype('int64') 
    data5=data5.astype('str')
    data6=(data4[['Te Vdekur']])
    data6=data6.astype('int64') 
    data6=data6.astype('str')
    data7=(data4[['Te Vdekur']])
    data7=data7.astype('int64') 
    data7=data7.astype('str')
    data8=(data4[['Te Testuar']])
     
    data8=data8.astype('str')
    data9=(data4[['Numri i Popullesise']])
    data9=data9.astype('int') 
    
    data9=data9.astype('str')
    data10=(data4[['Te vaksionuar me nje doze']])
    
    data10=data10.astype('str')
    data11=(data4[['Te vaksionuar me dy doza']])
    
    data11=data11.astype('str')
    data12=(data4[['Numri i pergjitheshem i vdekjeve deri me daten e caktuar:']])
    data12=data12.astype('int64') 
    data12=data12.astype('str')
   
    return render_template('Covid.html',prediction_text2='{}'.format(data5[['Raste e Reja']]) +'  '+'Persona',prediction_text='Data {}'.format(Numri2),
    prediction_text3='{}'.format(data6[['Te Vdekur']])+'  '+'Persona',
    prediction_text1='{}'.format(data8[['Te Testuar']])+'  '+'Persona',
    prediction_text4='{}'.format(data9[['Numri i Popullesise']])+'  '+'Persona',
    prediction_text5='{}'.format(data10[['Te vaksionuar me nje doze']])+'  '+'Persona',
    prediction_text6='{}'.format(data11[['Te vaksionuar me dy doza']])+'  '+'Persona',
    prediction_text7='{}'.format(data12[['Numri i pergjitheshem i vdekjeve deri me daten e caktuar:']])+' -- '+'Persona te vdekur')
    
    
    
if __name__ == '__main__':
    app.run(debug=True)