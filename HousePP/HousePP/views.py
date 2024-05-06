from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score

# import joblib
# from joblib import dump, load
# model2=joblib.load(r'C:\Users\Dhanraj Banglurkar\Desktop\Hpp\HousePP\model\banglore_home_price_model.pkl')


def index(request):
    return render(request, "index.html")

def ba(request):
    return render(request, "ba.html")

def aboutus(request):
    return render(request, "aboutus.html")

# def contact(request):
#     return render(request, "contact.html")

def prediction(request):

    d4 = pd.read_csv(r'C:\Users\Dhanraj Banglurkar\Desktop\House_price\LMN.csv')
    # Fetch unique locations from the dataset
    locations = d4['location'].unique().tolist()

    # Pass the locations to the template context
    context = {'locations': locations}

    # return render(request, 'your_template.html', context)
    return render(request, "prediction.html",context)

def result(request):
    d8 = pd.read_csv(r'C:\Users\Dhanraj Banglurkar\Desktop\House_price\py.csv')
    d4 = pd.read_csv(r'C:\Users\Dhanraj Banglurkar\Desktop\House_price\LMN.csv')
    # Fetch unique locations from the dataset
    locations = d4['location'].unique().tolist()


    a = d8.drop('price', axis='columns')
    y = d8.price
    x_train, x_test, y_train, y_test = train_test_split(a, y, test_size=0.2)
    model2 = RandomForestRegressor(n_estimators=50, random_state=42)
    model2.fit(x_train, y_train)

    def price_predict(location, area, bhk, resale, furnished, school, security, carparking, hospital, playarea, liftavailable, vaastucompliant):
        loc_index = np.where(a.columns == location)[0][0]

        x = np.zeros(len(a.columns))
        x[0] = area
        x[1] = bhk
        x[2] = resale
        x[3] = furnished
        x[4] = school
        x[5] = security
        x[6] = carparking
        x[7] = hospital
        x[8] = playarea
        x[9] = liftavailable
        x[10] = vaastucompliant
        if loc_index >= 0:
            x[loc_index] = 1

        return model2.predict([x])[0]

    if request.method == 'GET':
        var1 = str(request.GET.get('L1', ''))
        var2 = float(request.GET.get('L2', 0))
        var3 = float(request.GET.get('L3', 0))
        var4 = int(request.GET.get('a1', 0))
        var5 = int(request.GET.get('a2', 0))
        var6 = int(request.GET.get('a3', 0))
        var7 = int(request.GET.get('a4', 0))
        var8 = int(request.GET.get('a5', 0))
        var9 = int(request.GET.get('a6', 0))
        var10 = int(request.GET.get('a7', 0))
        var11 = int(request.GET.get('a8', 0))
        var12 = int(request.GET.get('a9', 0))

    pred = price_predict(var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12)
    pred = round(pred)

    price = "Estimated price of Your Residence is Rs"+str(pred)+"(Lakhs)"
    context = {'result2': price,'locations': locations}
    return render(request, "prediction.html", context)
