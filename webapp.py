from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/") #annotation tells the url that will make this function run
def render_main():
    return render_template('home.html')
    # 1: Looks for, creates, and sets global variables in template
    # 2: Content from blocks in child copied into layout template
    # 3: If statements run
    # 4: Final rendered HTML send to client

@app.route("/page1")
def render_page1():
    return render_template('page1.html')

@app.route("/page2")
def render_page2():
    return render_template('page2.html')

if __name__=="__main__":
    app.run(debug=False, port=54321)
