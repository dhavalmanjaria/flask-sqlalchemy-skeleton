from data import db

class HistoricalData(db.Model):
    """Represents a simple OHLCV table with a symbol    
    """

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime)
    symbol = db.Column(db.String)
    open = db.Column(db.Numeric)
    high = db.Column(db.Numeric)
    low = db.Column(db.Numeric)
    close = db.Column(db.Numeric)
    volume = db.Column(db.Integer)


class Users(db.Model):
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    age = db.Column(db.Integer)