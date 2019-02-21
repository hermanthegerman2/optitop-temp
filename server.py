import connexion
from flask import render_template
from connexion.resolver import RestyResolver

# Create the application instance


# Read the swagger.yml file to configure the endpoints
# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app = connexion.App(__name__, debug=True, 5000, specification_dir='./')
    app.add_api('swagger.yml', resolver=RestyResolver('api'))
    app.run()

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

