import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html',
                           title="Landing Page")


@app.route('/about')
def about():
    return render_template('about.html',
                         title="About Us")





if __name__ == '__main__':
    # Watch for changes in the 'templates' and 'static' directories
    extra_dirs = ['templates/', 'static/']  # Adjust paths as needed
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = os.path.join(dirname, filename)
                if os.path.isfile(filename):
                    extra_files.append(filename)
    app.run(debug=True, extra_files=extra_files)