import streamlit as stlt
import pickle
import numpy as np
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
stlt.title("LAPTOP PRICE PREDICTION")
company=stlt.selectbox('Brand',df['Company'].unique())

TypeName=stlt.selectbox('Type',df['TypeName'].unique())

Ram=stlt.selectbox("Ram in GB's",[2,4,6,8,12,16,24,32])

Weight=stlt.number_input('Weight of the laptop')

Touchscreen=stlt.selectbox('Touchscreen',['No','Yes'])

IPS=stlt.selectbox('Ips',['No','Yes'])

ScreenSize=stlt.number_input('Screen Size')

Resol=stlt.selectbox('Screen Resolution',['1920x1080',
'1366x768','1600x900','3840x2160','2880x1880','2560x1600','2304x1440'])


CPU=stlt.selectbox('CPU',df['CPU Brand'].unique())

HDD=stlt.selectbox('HDD in GB',[0,128,256,512,1024,2048])

SDD=stlt.selectbox('SDD in GB',[0,8,128,256,512,1024])

GPU =stlt.selectbox('GPU',df['Gpu brand'].unique())

Os=stlt.selectbox('OS',df['os'].unique())

if stlt.button('Predict Price'):
    PPI=None
    if Touchscreen=='Yes':
        Touchscreen=1
    else:
        Touchscreen = 0

    if IPS=='Yes':
        IPS=1
    else:
        IPS = 0

    X_res=int(Resol.split('x')[0])
    Y_res = int(Resol.split('x')[1])
    PPI=((X_res**2)+(Y_res**2))**0.5/ScreenSize
    query =np.array([company,TypeName,Ram,Weight,Touchscreen,IPS,PPI,CPU,HDD,SDD,GPU,Os])

    query =query.reshape(1,12)
    my_num =int(np.exp(pipe.predict(query)[0]))
    s = "{:,}".format(my_num)

    stlt.title(company+" laptop Price is "+str(s))
    # stlt.title("laptop Price Prediction is " + str( int(np.exp(pipe.predict(query)[0]))))