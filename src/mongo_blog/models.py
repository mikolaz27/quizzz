import datetime

from mongoengine import (
    StringField, ListField, DateTimeField, Document, EmbeddedDocumentField,
    EmbeddedDocument
)


class Blog(EmbeddedDocument):
    name = StringField(max_length=255)
    text = StringField()


class Entry(Document):
    blog = ListField(EmbeddedDocumentField(Blog))
    timestamp = DateTimeField(default=datetime.datetime.now())
    headline = StringField(max_length=255)
