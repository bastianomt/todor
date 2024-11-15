from todor import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text(20), nullable=False)

    def __init__(self, username, password):
        self.username = username,
        self.password = password
    
    def __repr__(self):
        return f'<User: {self.username} >'

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_By = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200))
    state = db.Column(db.Boolean, default=False)

    def __init__(self, created_By, title, desc, state):
        self.created_By = created_By,
        self.title = title,
        self.desc = desc,
        self.state = state

    def __repr__(self):
        return f'<Todo: {self.title} >'