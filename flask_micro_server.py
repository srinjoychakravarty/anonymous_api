"""
Main module of the server file
"""
# local modules
import config

# Get the application instance
connex_app = config.connexion_application

# Read the swagger.yml file to configure the endpoints
connex_app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@connex_app.route('/')
def home():
    """
    This function responds to the browser URL localhost:5000/ i.e. the root landing page
    """

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    connex_app.run(debug = True)
