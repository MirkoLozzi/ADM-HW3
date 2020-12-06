# ADM-HW3

![alt text](https://camo.githubusercontent.com/406644a4e60cd793ef853c47ee30ec2206f3b87081731fb80976824b56417a41/68747470733a2f2f73323938322e7063646e2e636f2f77702d636f6e74656e742f75706c6f6164732f323031352f31322f676f6f6472656164732d65313435373535353432343738302e6a70672e6f7074696d616c2e6a7067)

#### **Description of the tasks**

In this homework we build a dataset from scratch by collecting information about books from [goodreads](https://www.goodreads.com/), site for readers and book recommendations.
We downloaded the url’s connetted to the first 300 pages of the most loved books and their HTML file where we stored Information about the book.
This Information was then parsed to mantain only what was relevant to us, such as book title, author name, and plot. Then , it was saved in a unique tsv file ```Books.tsv```.
You can retrieve the code to perform this task in the python notebook ```Download_and_parsing.ipynb```.

We build two different search engines wich retrives the books title, plot and links of the documents that contain the input query of the user. The first one gives us the documents that contain all the words in the input query,  while the second search engine will retrive the top-k documents sorted by the cosine similarity evaluated over TF-IDF.


Also we studied the cumulative numer of page during time, of the top-10 book series in the catalogue.

Finally we answered the algorithmic question about the longest common sub-sequence. Showing the exponential running time of the recursive algorithm can be improoved using dynamic progamming.

#### **Content**

* ```main.ipynb```: In this file there are the code about the search engines, and the questions 3, 4 and 5.
* ```Download_and_parsing.ipynb```: We saved in this file all the code we used to download and parse information about the books.
* ```Function.py```: Where it's possible to find all the functions concernig the parsing, and question 4 and 5.
* ```search_engine.py```: In this file there are all the functions to run the search engines








