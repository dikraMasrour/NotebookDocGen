import argparse
import preprocessor as prep
import embedder as e
import dom_model_invoker as dmi
import tech_model_invoker as tmi


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
    parser.add_argument('-c', "--classification", type=str, choices=('domain', 'technique', 'both'), help = "Type of classification")
    # Read arguments from command line
    args = parser.parse_args()
    dom = None
    tech = None
    if args.path:
        
        
        
        if prep.check_ipynb(args.path):
            print('Invalid notebook format. Please provide a .ipynb file')
            exit()


        clean_df = prep.preprocess(args.path)
        # print(clean_df)
        vect_ntb = e.embed(clean_df)
        # print(vect_ntb, vect_ntb.shape, vect_ntb.describe())
        

        if args.classification == 'domain':      
            dom = dmi.domain_classification(vect_ntb)
        
        if args.classification == 'technique':      
            tech = tmi.technique_classification(vect_ntb)
            
        if args.classification == 'both':      
            tech = tmi.technique_classification(vect_ntb)
            dom = dmi.domain_classification(vect_ntb)


    class_tuple = (dom, tech)
    print(class_tuple)

if __name__ == "__main__":
    main()