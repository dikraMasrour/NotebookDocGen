# NotebookDocGen

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Description">Description</a></li>
    <li><a href="#Contributors">Contributors</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Tech-Stack">Tech Stack</a></li>
    <li><a href="#Demo">Demo</a></li>
    <li><a href="#Classification-Task">Classification Task</a>
        <ul>
            <li><a href="#Data-Collection">Data Collection</a></li>
            <li><a href="#Data-Cleaning-and-preprocessing">Data Cleaning and preprocessing</a></li>
            <li><a href="#Embedding-using-codeBert">Embedding using codeBert</a></li>
            <li><a href="#Classification-experiements">Classification experiements</a></li>
      </ul>
    </li>
    <li><a href="#Documentation-generation-Task">Documentation generation Task</a>
        <ul>
            <li><a href="#Data-Collection">Data Collection</a></li>
            <li><a href="#Data-Cleaning-and-preprocessing">Data Cleaning and preprocessing</a></li>
            <li><a href="#Data-transformation">Data transformation</a></li>
            <li><a href="#PLBART">PLBART</a></li>
            <li><a href="#Pairs-construction">Pairs construction</a></li>
      </ul>
    </li>
  </ol>
</details>


## Description
Our machine learning project consists of building a tool that improves Data Science & Machine Learning experts and learners’ experience of writing notebooks and organizing them. The features include: the classification of the notebooks by ML domains it belongs to (NLP, computer vision and reinforcement learning), and techniques it uses (classification, clustering and regression). As well as the automatic generation of documentation for individual code cells in a notebook.
As for the tools used, we respectively applied the pre-trained **CodeBERT** model alongside a Classifier (created locally & under Oracle AutoML) for the classification task, and a **PLBART** model for the documentation generation task.
All these features are showcased in a Streamlit web application offering users the opportunity to test and explore them.


<p align="right">(<a href="#readme-top">⬆️</a>)</p>

## Contributors

- [dikraMasrour](https://github.com/dikraMasrour)
- [D-Zineb](https://github.com/D-Zineb)

<p align="right">(<a href="#readme-top">⬆️</a>)</p>

## Features

- Classification of the notebooks by ML domains : **NLP** , **Computer Vision** and **Reinforcement Learning**.
- Classification of the notebooks by ML techniques : **Regression** , **Classification** and **Clustering**.
- Automatic generation of documentation for individual code cells for a notebook.

<p align="right">(<a href="#readme-top">⬆️</a>)</p>

## Tech Stack

**Data Analysis :** Pandas, numpy, regex, plotly, matplotlib, seaborn, nltk, tokenize...

**Modeling :** Torch,scikit-learn

**Deployement :** Streamlit

<p align="right">(<a href="#readme-top">⬆️</a>)</p>

## Demo

[Link]()

<p align="right">(<a href="#readme-top">⬆️</a>)</p>

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

### Classification experiements

- Local experiements with different classification models .
- Used ***Oracle*** **AutoML** :  Oracle Machine Learning interface that provides you no-code automated machine learning .
- Best model gives about : **86%** accuracy .


### Link to our dataset

- [Final_Classification_Dataset]()

<p align="right">(<a href="#readme-top">⬆️</a>)</p>


## Documentation generation Task

### Data Collection

- Collect suitable notebooks from Kaggle courses .
- Collect **top voted** notebooks from **getting started** competitions on Kaggle .

### Data Cleaning and preprocessing

- Remove non-english and non-python notebooks .
- Parse JSON notebooks into Dataframe containing notebooks content and  tag.
- Clean the Data by removing special characters, spelling checker, non-python code ,emojis ... While being careful to keep punctuation .
- Create markdown and code pairs .

### Data Transformation

We have about **~3000** code cells that have comments included and **9633** is the total number of comments .Those comments can have even more precise and accurate documentation for code than markdowns that can be more general .So we've extracted comments from code cells and mark them as markdown while keeping the order of notebook's cells.

### Pairs construction

- First strategy consists into grouping all markdowns cells that follow each other and group them into one markdown ,we do the same for code cells .And then we build pairs based on markdown cell and code cell that follow each other .

- Second strategy consists into grouping only markdown and code cells that follow each other into one pair .

### PLBART

By first use of PLBART model without finetunning , we got an Overall *Mean bert_score*  :   **0.74** .


### Link to our dataset
- [Final_DocGen_Dataset]()

<p align="right">(<a href="#readme-top">⬆️</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/dikraMasrour/NotebookDocGen.svg?style=for-the-badge
[contributors-url]: https://github.com/dikraMasrour/NotebookDocGen/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dikraMasrour/NotebookDocGen.svg?style=for-the-badge
[forks-url]: https://github.com/dikraMasrour/NotebookDocGen/network/members
[stars-shield]: https://img.shields.io/github/stars/dikraMasrour/NotebookDocGen.svg?style=for-the-badge
[stars-url]: https://github.com/dikraMasrour/NotebookDocGen/stargazers
[issues-shield]: https://img.shields.io/github/issues/dikraMasrour/NotebookDocGen.svg?style=for-the-badge
[issues-url]: https://github.com/dikraMasrour/NotebookDocGen/issues
