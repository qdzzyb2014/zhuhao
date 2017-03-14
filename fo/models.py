from datetime import datetime as dt
from .extensions import db


Column = db.Column


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class Model(CRUDMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""

    __abstract__ = True


class User(Model):
    __tablename__ = 'zhuhao_users'

    id = Column(db.INTEGER, primary_key=True)
    name = Column(db.Unicode, unique=True)
    password = Column(db.String(128))

    def __repr__(self):
        return '<user: {}>'.format(self.name)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class Registration(Model):
    __tablename__ = 'zhuhao_registrations'

    id = Column(db.INTEGER, primary_key=True)
    name = Column(db.Unicode, nullable=False)
    company = Column(db.Unicode, nullable=False)
    job_title = Column(db.Unicode)
    contact_way = Column(db.Unicode, nullable=False)
    main_industry = Column(db.Unicode)
    created = Column(db.TIMESTAMP, nullable=False, default=dt.now())
