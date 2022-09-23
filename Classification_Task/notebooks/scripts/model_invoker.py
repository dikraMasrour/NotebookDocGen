import pickle

FILE_DOM = 'C:\\Users\\dmasrour\\Documents\\CodeDoc_Generation\\Tasks\\Classification_Task\\models\\logr_domain_classification_OS_90.sav'
DOM_MODEL = pickle.load(open(FILE_DOM, 'rb'))


FILE_TECH = 'C:\\Users\\dmasrour\\Documents\\CodeDoc_Generation\\Tasks\\Classification_Task\\models\\logr_technique_classification_OS_79.sav'
TECH_MODEL = pickle.load(open(FILE_TECH, 'rb'))


def domain_classification(vect_ntb):
    return DOM_MODEL.predict(vect_ntb)[0]
    

def technique_classification(vect_ntb):
    return TECH_MODEL.predict(vect_ntb)[0]
    


