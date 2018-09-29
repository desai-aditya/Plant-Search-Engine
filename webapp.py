from flask import Flask, request, render_template ,  send_from_directory
import os
import string
import nltk
import math
import operator
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

def preprocess(text):
    tokens = word_tokenize(text)
    tokens = [w.lower() for w in tokens]
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    lem = WordNetLemmatizer()
    words_lem = [lem.lemmatize(w) for w in words]
    return words_lem

dic = {}
f = open("./data/plantslist.txt", "r")
lines = f.readlines()
doc = []
for l in lines:
    doc.append(l.split('\n')[0].split('/')[-1])

for d in doc:
    flnm = './data/'+d+'.txt'
    file = open(flnm, 'rt')
    text = file.read()
    file.close()
    words_lem = preprocess(text)

    # building inverted index
    for wl in words_lem:
        if wl in dic:
            if d in dic[wl]:
                dic[wl][d] += 1
            else:
                dic[wl][d] = 1
        else:
            dic[wl] = {}
            dic[wl][d] = 1

# computing tf-idf
N = len(dic)
for key1,value1 in dic.items():
    # print(value)
    lth = len(value1)
    for key, value in value1.items():
        idf = math.log(N/lth)
        dic[key1][key] = value*idf



app = Flask(__name__)

@app.route('/')
def webapp_form():
    return render_template('webapp-form.html')

@app.route('/list', methods=['POST'])
def webapp_form_post():
    # take query input from the user
    query = request.form['query']

    # preprocessing the query
    words_lemq = preprocess(query)

    # computing the score(q, d)
    final_docs = {}
    for wlq in words_lemq:
        if wlq in dic:
            for val, key in dic[wlq].items():
                if val in final_docs:
                    final_docs[val] += key
                else:
                    final_docs[val] = key

    sorted_x = sorted(final_docs.items(), key=operator.itemgetter(1), reverse=True)
    sorted_x = sorted_x[:10]
    list_of_paths = []
    for sx in sorted_x:
        temp = './data/'+sx[0]+'.txt'
        list_of_paths.append(temp)

    return  render_template('list.html', top_pages=list_of_paths)

@app.route('/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory= os.getcwd(), filename=filename, as_attachment=True)
