from peewee import Model, DateTimeField, OperationalError, CharField, \
    IntegerField
from playhouse.sqlite_ext import SqliteExtDatabase
from datetime import datetime

db = SqliteExtDatabase('teapot.db')


class BaseModel(Model):
    class Meta:
        database = db


class State(BaseModel):
    """Table that records the state of the teapot over time, commonly queried
    for the latest entry to tell people about the state of the teapot
    """
    state = CharField()
    timestamp = DateTimeField(default=datetime.now, index=True)
    num_of_cups = IntegerField()

    @classmethod
    def get_newest_state(cls):
        """Returns the row from the State table with the newest timestamp
        that represents the last known state of the teapot.

        Args:
            - None
        Returns:
            - state (State) - Row containing details on the state of the teapot
        """
        try:
            return State.select().order_by(-State.timestamp)[0]
        except IndexError:
            return None


if __name__ == "__main__":
    try:
        State.create_table()
    except OperationalError:
        print "The table already exists"