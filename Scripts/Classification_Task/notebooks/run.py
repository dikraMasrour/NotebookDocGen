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



def main():

    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("path", help = "Path to Notebook")
    # Read arguments from command line
    args = parser.parse_args()
    if args.path:
        
        
        if prep.check_ipynb(args.path):
            print('Invalid notebook format. Please provide a .ipynb file')
            exit()


        clean_df = prep.preprocess(args.path)
        print(clean_df)
        vect_ntb = e.embed(clean_df)
        print(vect_ntb, vect_ntb.shape, vect_ntb.describe())

        mi.modelling(vect_ntb)
        


if __name__ == "__main__":
    main()
