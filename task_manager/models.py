from task_manager import db
from task_manager import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    completed = db.Column(db.Integer, default=0)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task {}>'.format(self.id)