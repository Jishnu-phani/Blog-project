from flask import Flask, render_template
import requests
from post import Post

data = requests.get("https://api.npoint.io/a05aec98278e1703a81d").json()
app = Flask(__name__)
post_objects = []
for i in data:
    post_obj = Post(i["id"], i["title"], i["subtitle"], i["body"], i["author"], i["date"], i["photo-url"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", data=post_objects)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:index>')
def show_post(index):
    required_post = None
    for j in post_objects:
        if j.id == index:
            required_post = j
    return render_template("post.html", post=required_post)


app.run(debug=True)
