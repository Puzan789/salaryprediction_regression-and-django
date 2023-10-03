from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from .forms import ExperienceForm
import os
# Create your views here.

def index(request):
    csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'salarydata.csv')
    df=pd.read_csv(csv_file_path,usecols=['Years of Experience','Salary'])
    df.dropna(inplace=True)
    X=df[['Years of Experience']]
    y=df[['Salary']]
    X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.1,random_state=30)
    regressor=LinearRegression()
    regressor.fit(X_train,Y_train)
    context={}
    fm=ExperienceForm(request.GET)
    if fm.is_valid():
        years_of_experience = fm.cleaned_data['years_of_experience']
        ps=regressor.predict([[years_of_experience]])
        context['predictedsalary'] = round(ps[0][0], 2)  
    context['fm']=fm
    return render(request,'salarys/index.html',{"context":context})

