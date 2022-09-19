import argparse
import preprocessor as prep
import embedder as e
import model_invoker as mi

'''
- pass notebook to preprocessor as json in args + test if cells are a list + test if nb is .ipynb + test if english nb
- extract cells from nb
- remove raw cells
- clean markdowns & non english
- clean code cells

'''

'''
- record time
- add args option to consider md and code or code only
'''





def main(tempfile_notebook):

    
    if prep.check_ipynb(tempfile_notebook[0].name):
        print('Invalid notebook format. Please provide a .ipynb file')
        exit()


    clean_df = prep.preprocess(tempfile_notebook[0].name)

    vect_ntb = e.embed(clean_df)

    return mi.domain_classification(vect_ntb), mi.technique_classification(vect_ntb)
        
