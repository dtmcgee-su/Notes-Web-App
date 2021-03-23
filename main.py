from website import create_app

app = create_app()

#Only if we run this file, run the web server
if __name__ == '__main__':
    app.run(debug=True) #Anytime we make a change to python code, it will rerun the server. Very useful when editing. Will turn off when project is complete.

  