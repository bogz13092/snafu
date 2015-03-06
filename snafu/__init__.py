from flask import Flask

def create_app(cfg):
	app = Flask(__name__)
	app.config.from_pyfile(cfg)
	print __name__

	from snafu.blueprints.user import user_bp
	app.register_blueprint(user_bp)
	return app