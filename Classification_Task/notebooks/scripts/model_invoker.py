import pickle



def domain_classification(vect_ntb):
    filename = 'D:\\Oracle_ML_Project_data\\Classification_Task\\models\\logr_domain_classification.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model.predict(vect_ntb)[0]
    


def technique_classification(vect_ntb):
    filename = 'D:\\Oracle_ML_Project_data\\Classification_Task\\models\\logr_technique_classification.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model.predict(vect_ntb)[0]
    


