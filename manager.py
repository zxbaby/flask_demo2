#!/usr/bin/env python
#coding=utf-8
from flask import g
from flask_login import current_user
from flask.ext.script import Manager
from apps import create_app
from flask_migrate import Migrate, MigrateCommand
from apps.init import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.before_request
def before_request():
    g.user = current_user


@manager.command
def test():
    pass

@manager.command
def deploy():
    pass

@manager.command
def main():
    server_ip = '0.0.0.0'
    server_port = 40000
    app.run(host=server_ip, port=server_port, debug=True)

if __name__ == '__main__':
#    main()
    manager.run()
