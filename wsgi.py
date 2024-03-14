from run import app

if __name__ == "__main__":
    app.run()


#gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
#curl -X POST -H "Content-Type: application/json" -d '{"start": [1, 2], "target": [3, 4]}' http://127.0.0.1:5000/api
