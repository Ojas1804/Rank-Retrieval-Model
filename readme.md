Create Folders:
    For program to work, you need to create folders Dataset, Indexes, and tfidf_weights
    else it would throw an error. Store dataset in Dataset folder. Program will find 
    posting lists and store it in Indexes folder. tfidf_weights folder will store tfidf
    weights of each document.

This assignment has 7 python files and 4 folders. The 7 python files are:
- CosineSimilarity.py: Calculated cosine similarity between document and query.
- Lemmatizer.py: Lemmatizes the words in the document.
- main.py: Main program to run the program.
- PostingList.py: Creates posting list for each word in the document.
- PreprocessQuery.py: Preprocesses the query.
- Stopwords.py: Removes stopwords from the document.
- TfIdf.py: Calculates tfidf weights for each document and query.

To test this assignment, run the main.py file. It will ask for query and will return top 10 documents with highest cosine similarity.
