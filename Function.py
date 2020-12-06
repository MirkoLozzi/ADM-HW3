import re
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import numpy as np
import matplotlib.pyplot as plt


'''
Function question 4

'''

def replace_all(x, array):
    for i in array:
        x = x.replace(i, '')
    return x

def check_single_book(x):
    find_1 = re.compile(r'[0-9]-[0-9]') #minus symbol
    find_2 = re.compile(r'[0-9]–[0-9]') #dash symbol
    if len(x.split('#')) == 2:
        if re.match(find_1, x.split('#')[1]) or re.match(find_2, x.split('#')[1]):
            return 0
        else:
            return 1
    else:
        return 1
    
def clean_series(x):
    return x.split('#')[0].strip()

def detect_stable(s):
    if type(s) == str:
        try:
            l = detect(s)
            return l
        except LangDetectException as e:
            return None
    else:
        return None
    
def nrBooksPerSeries(books, x):
    return len(books[books.bookSeries == str(x)])

def Plot_Cumulative_page(Series, book_analysis):
    Year = list(range(book_analysis.PublishingDate.max()+1))

    All_Series_page = {}

    for name in Series:
        page = np.zeros(book_analysis.PublishingDate.max()+1)

        page[book_analysis[book_analysis.bookSeries == name].PublishingDate.values] =\
        book_analysis[book_analysis.bookSeries == name].NumberofPages.values

        All_Series_page[name] = page
        
    plt.figure(figsize=(12, 7))
    for key in All_Series_page.keys():
        plt.plot(Year, np.cumsum(All_Series_page[key]), label = key, linewidth = 4)

    plt.legend()
    plt.show()
    
    return None