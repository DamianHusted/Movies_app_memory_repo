from Movie_app.app import app

if __name__ == "__main__":
    app.run(host='localhost', port=1337, threaded=False, debug=True)