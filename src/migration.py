from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

MIGRATION_DIR = './database/migrations'

migrate = Migrate(app, db, directory=MIGRATION_DIR)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

from models import user

if __name__ == "__main__":
     manager.run()