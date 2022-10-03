# NotebookCodeGen

## Description
Our machine learning project consists of building a tool that improves Data Science & Machine Learning experts and learners’ experience of writing notebooks and organizing them. The features include: the classification of the notebooks by ML domains it belongs to (NLP, computer vision and reinforcement learning), and techniques it uses (classification, clustering and regression). As well as the automatic generation of documentation for individual code cells in a notebook.
As for the tools used, we respectively applied the pre-trained **CodeBERT** model alongside a Classifier (created locally & under Oracle AutoML) for the classification task, and a **PLBART** model for the documentation generation task.
All these features are showcased in a Streamlit web application offering users the opportunity to test and explore them.


## Contributors

- [dikraMasrour](https://github.com/dikraMasrour)
- [D-Zineb](https://github.com/D-Zineb)

## Features

- Classification of the notebooks by ML domains : **NLP** , **Computer Vision** and **Reinforcement Learning** .
- Classification of the notebooks by ML techniques : **Regression** , **Classification** and **Clustering** .
- Automatic generation of documentation for individual code cells for a notebook .

## Tech Stack

**Data Analysis :** Pandas,numpy,regex,plotly,matplotlib,seaborn,nltk,tokenize...

**Modeling :** Torch,scikit-learn

**Deployement :** Streamlit

## Demo

[Link]()

## Classification Task

### Data Collection

- Build list of keywords for each domain and technique : [List_Keywords](https://github.com/dikraMasrour/NotebookDocGen/blob/main/Classification_Task/data/search_keywords.csv) .

- Collect about **10463** notebooks from Kaggle based on research of keywords .

### Data Cleaning and preprocessing

- Remove non-english, non-python and duplicate notebooks .
- Parse JSON notebooks into Dataframe containing notebooks content and  tag.
- Clean the Data by removing punctuation, special characters, spelling checker, non-python code ,emojis ...

### Embedding using codeBert

Embed **332605** markdown and code cells using ***codeBert*** .

### Classification 

- Local experiements with different classification models .
- Used ***Oracle*** **AutoML** :  Oracle Machine Learning interface that provides you no-code automated machine learning .
- Best model gives about : **86%** accuracy .


### Link to our dataset

- [Final_Classification_Dataset]()


## Documentation generation Task

### Data Collection

- Collect suitable notebooks from Kaggle courses .
- Collect **top voted** notebooks from **getting started** competitions on Kaggle .

### Data Cleaning and preprocessing

- Remove non-english and non-python notebooks .
- Parse JSON notebooks into Dataframe containing notebooks content and  tag.
- Clean the Data by removing special characters, spelling checker, non-python code ,emojis ... While being careful to keep punctuation .
- Create markdown and code pairs .

### PLBART

By first use of PLBART model without finetunning , we got an Overall *Mean bert_score*  :   **0.74** .


### Link to our dataset
- [Final_DocGen_Dataset]()

