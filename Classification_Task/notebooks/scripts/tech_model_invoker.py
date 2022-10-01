import pickle


FILE_TECH = r'..\Classification_Task\models\finalized_model_improved_os.sav'
TECH_MODEL = pickle.load(open(FILE_TECH, 'rb'))




def technique_classification(vect_ntb):
    print('ran tech part')
    return TECH_MODEL.predict(vect_ntb)[0]
    


