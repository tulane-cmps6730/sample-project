# Getting Started

This document aims to help you to:

- familiarize yourself with many of the tools we will be using throughout this project
- understand the three problem tasks definitions
- learn how to use the Twitter API to collect data
- parse and compute statistics of the labeled training data
- use flask to make a simple web form

<br>


### Getting Started with your Github Repository.

You should have been assigned a project repository for your work. In the examples below, we'll assume the repository is called <https://github.com/tulane-cmps6730/sample-project>. This is where all your code will live. 

Your repository has been setup with a lot of starter code so you can get started more easily. To use it, do the following:

1. Make sure you've completed all the course **Background Resources** listed on the [README](https://github.com/tulane-cmps6730/sample-project/blob/main/README.md).
2. Clone your repo:  `git clone https://github.com/nlp/sample-project`
3. Start a [virtual environment](https://virtualenv.pypa.io/en/stable/).
  - First, make sure you have virtual env installed. `pip install virtualenv`
  - Next, outside of the team repository, create a new virtual environment folder by `virtualenv nlp-virtual`. 
  - Activate your virtual environment by `source nlp-virtual/bin/activate`
  - Now, when you install python software, it will be saved in your `nlp-virtual` folder, so it won't conflict with the rest of your system.
4. Install your project code by
```
cd sample-project   # enter your project repository folder
pip install -r requirements.txt
python setup.py develop # install the code. 
```

This may take a while, as all dependencies listed in the `requirements.txt` file will also be installed.

**Windows users**: if you're having troubles, try reading [this](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/). It looks like you will need to:
- install `pip install virtualenvwrapper-win`
- instead of `virtualenv nlp-virtual` above, do `mkvirtualenv nlp-virtual`
- other students have also had luck starting environments with the command `py -3 -m venv env env\scripts\activate`

5. If everything worked properly, you should now be able to run your project's command-line tool by typing:  
```
nlp --help
```
which should print
```
Usage: nlp [OPTIONS] COMMAND [ARGS]...

  Console script for nlp.

Options:
  --help  Show this message and exit.

Commands:
  dl-data  Download training/testing data.
  stats    Read the data files and print interesting statistics.
  train    Train a classifier and save it.
  web      Launch the flask web app
```

### Flask Web UI

Your tool currently has one command called `web`. This launches a simple web server which we will use to make a demo of your project. You can launch it with:  
`nlp web`  
which should produce output like:
```
read clf LogisticRegression(C=1, class_weight='balanced', max_iter=1000)
read vec CountVectorizer(binary=True, min_df=5, ngram_range=(1, 3), stop_words='english')
 * Serving Flask app "nlp.app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
read clf LogisticRegression(C=1, class_weight='balanced', max_iter=1000)
read vec CountVectorizer(binary=True, min_df=5, ngram_range=(1, 3), stop_words='english')
 * Debugger is active!
 * Debugger PIN: 128-371-422
```

If you open your web browser and go to `http://0.0.0.0:5000/` you should see something like:

![web.png](web.png)



**Tips:**
- Some web browsers will cache the page, which will sometimes make it hard to see the updates you make. You may have to force a refresh that ignores the cache (e.g. see [here for Chrome](https://superuser.com/questions/89809/how-to-force-refresh-without-cache-in-google-chrome)).
