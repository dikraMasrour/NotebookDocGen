import pickle

FILE_DOM = '..\Classification_Task\models\logr_domain_classification_OS_90.sav'
DOM_MODEL = pickle.load(open(FILE_DOM, 'rb'))


def domain_classification(vect_ntb):
    print('ran dom part')
    return DOM_MODEL.predict(vect_ntb)[0]
    


