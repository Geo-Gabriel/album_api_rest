from album_api import app

if __name__ == '__main__':
    app.run(debug=True)

# flask-sqlacodegen --flask --outfile models.py mysql+pymysql://root:@localhost:3306/albuns
