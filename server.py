import connexion
from flask import render_template
from connexion.resolver import RestyResolver

# Create the application instance


# Read the swagger.yml file to configure the endpoints
# If we're running in stand alone mode, run the application

# Create a URL route in our application for "/"



if __name__ == '__main__':
    app = connexion.App(__name__, 5000, specification_dir='./')
    def home():
        """
        This function just responds to the browser ULR
        localhost:5000/
        :return:        the rendered template 'home.html'
        """
        return render_template('home.html')
    app.add_api('swagger.yml', resolver=RestyResolver('api'))
    app.run(host='0.0.0.0', debug=True)