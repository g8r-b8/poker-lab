from hapi.factory import create_app

import os
import configparser

def main():
    config = configparser.ConfigParser()
    config.read(os.path.abspath(os.path.join(".ini")))
    app = create_app()
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config['PROD']['DB_URI']
    app.run()

if __name__ == "__main__":
    main()

