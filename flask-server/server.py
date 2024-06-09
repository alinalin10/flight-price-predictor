from flask import Flask
import pandas as pd
import function
from sklearn.model_selection import train_test_split
import pickle



# loading model
loaded_model = pickle.load(open('/workspaces/new-project/model_0.sav', 'rb'))

# try out
data = function.try_data(0, 0, 2.17, 22, 'Indigo', 'Late_Night', 'Early_Morning', 'Delhi', 'Mumbai')
print(loaded_model.predict(data))

# app
app = Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["mem1", "mem2", "mem3"]}

if __name__ == "__main__":
    app.run(debug=True)


