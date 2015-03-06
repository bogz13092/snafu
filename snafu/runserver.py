from snafu import create_app
app = create_app('settings.cfg')
app.run()
