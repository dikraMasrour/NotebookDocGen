import pickle
from sklearn.linear_model import LogisticRegression

FILE_TECH = 'Classification_Task/models/finalized_model_improved_os.sav'
TECH_MODEL = pickle.load(open(FILE_TECH, 'rb'))




def technique_classification(vect_ntb):
    return TECH_MODEL.predict(vect_ntb)[0]
    


