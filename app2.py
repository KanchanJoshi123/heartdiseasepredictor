import joblib
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
model = joblib.load('model2.save')

@app.route('/')
def home():
    return render_template('Heartdiseaseform.html')

@app.route('/predict',methods=['POST'])
def predict():

    a=request.form["age"]
    b= request.form["gender"]
    if (b == 'Female'):
        b=0
    if (b == 'Male'):
        b=1
    c=request.form["cp"]
    if (c == 'TA'):
      c=0
    if (c == 'AA'):
      c=1
    if (c == 'NAP'):
      c=2
    if (c == 'A'):
      c=3
    d=request.form["trestbps"]
    e=request.form["cholestrol"]
    f=request.form["fbs"]
    if (f== 'g'):
      f=1
    if (f == 'l'):
      f=0
    g=request.form["restecg"]
    if (g == 'n'):
      g=0
    if (g == 'st'):
      g=1
    if (g == 'vh'):
      g=2
    h=request.form["thalach"]
    i=request.form["exang"]
    if (i == 'y'):
        i=1
    if (i == 'n'):
        i=0
    j=request.form["old peak"]
    k=request.form["slope"]
    if (k == 'us'):
      k=0
    if (k == 'fl'):
      k=1
    if (k == 'dn'):
      k=2
    l=request.form["ca"]
    m=request.form["thal"]
    if (m == 'nor'):
      m=1
    if (m == 'fd'):
      m=2
    if (m == 'rd'):
      m=3
    y=[[a,b,c,d,e,f,g,h,i,j,k,l,m]]        
    output = model.predict(y)
    if (output == 0):
    #if output == 0:
        res_val="a heart disease!"
        return render_template('Houtputpositive.html',predict='You might not have {}'.format(res_val))
    else:
        res_val="a heart disease."
        return render_template('Houtputpositive.html',predict='Sorry:( You may have {}'.format(res_val))
        
    #return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)