from flask import Flask ,request , render_template , url_for

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Importing stopwords from corpus
from nltk.corpus import stopwords

set(stopwords.words('english'))
#url = url_for('structure' ,filename='form.html')

app = Flask(__name__ , template_folder="structure")

@app.route('/')

def my_form():
    return render_template("form.html")
similarity_matrix = 0

@app.route('/' , methods = ['POST'])

def my_from_post():
    stop_words = stopwords.words('english')

    #The texts written in the form.html are converted to lowercase
    text1 = request.form['text1'].lower()  
    text2 = request.form['text2'].lower()

    # texts are then coverted to stop words
    processed_text1 = ' '.join([word for word in text1.split() if word not in stop_words])
    processed_text2 = ' '.join([word2 for word2 in text2.split() if word2 not in stop_words])
    corpus = [processed_text1 , processed_text2]

    #The processed texts are then vectorised and similarity matrix is then calculated
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)
    similarity_matrix = cosine_similarity(tfidf)[0][1]

    return render_template("form.html" ,final=similarity_matrix , text1 =text1 , text2=text2)


if __name__=="__main__":
    app.run(debug=True, threaded=True)

