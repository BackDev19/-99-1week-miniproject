from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ym6ab.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def web_write_post():
    title_receive = request.form['title_give']
    img_receive = request.form['img_give']
    comment_receive = request.form['comment_give']
    doc = {
        'title' : title_receive,
        'img' : img_receive,
        'comment' : comment_receive
    }
    db.App.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/submit", methods=["GET"])
def web_write_get():
    write_list = list(db.App.find({}, {'_id': False}))
    return jsonify({'orders': write_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)