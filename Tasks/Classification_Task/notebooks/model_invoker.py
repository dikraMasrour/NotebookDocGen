from pyexpat import model
import pycurl
from io import BytesIO
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, roc_auc_score, f1_score
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import pickle

''''curl -X POST "${omlserver}/omlmod/v1/deployment/svm_mpg/score" \
--header "Authorization: Bearer ${token}" \
--header 'Content-Type: application/json' \
-d '{"inputRecords":[{
  "cylinders":4,
  "displacement":68,
  "horsepower":49,
  "weight":1867,
  "acceleration":19.5,
  "model_year":73,
  "brand":"fiat",
  "Country":"Europe"
}]}'''


def modelling(vect_ntb):
    filename = 'C:\\Users\\dmasrour\\Documents\\CodeDoc_Generation\\Scripts\\Classification_Task\\notebooks\\finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    print(loaded_model.predict(vect_ntb)[0])



