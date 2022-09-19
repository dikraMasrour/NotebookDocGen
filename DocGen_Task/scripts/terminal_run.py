import doc_generator as dg
import argparse


def main():


     # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("path", help = "Path to Notebook")
    # Read arguments from command line
    args = parser.parse_args()

    if args.path:
        
        
        if dg.check_ipynb(args.path):
            print('Invalid notebook format. Please provide a .ipynb file')
            exit()




    return dg.document_notebook(args.path)





if __name__ == "__main__":
    main()