from connexion.resolver import RestyResolver


import config


connexion_app = config.connexion_app
connexion_app.add_api('swagger_small.yaml', resolver=RestyResolver('api'))


if __name__ == "__main__":
    connexion_app.run(debug=True)
