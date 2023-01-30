import connexion
import logging

def create_app():
    logging.basicConfig(level=logging.DEBUG)
    connex_app = connexion.FlaskApp(__name__, specification_dir="./swagger/")
    connex_app.add_api("./edscorbot.yaml", resolver_error=501)
    return connex_app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)