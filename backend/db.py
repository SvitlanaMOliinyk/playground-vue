from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()

def init_db_and_tables(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        inspector = inspect(db.engine)
        table_names = inspector.get_table_names()
        for table_name in table_names:
            print(f"Table: {table_name}")
