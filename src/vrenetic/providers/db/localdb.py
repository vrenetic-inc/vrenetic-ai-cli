import pprint
from tinydb import TinyDB, Query

def getById(id):
    Item = Query()
    db = TinyDB('./data/db.json')
    table = db.table('models')
    application_config = table.search(Item.id.matches(id))
    return application_config

def getAll():
    Item = Query()
    db = TinyDB('./data/db.json')
    table = db.table('models')
    application_config = table.search(Item.application.matches(""))
    return application_config
    # table.insert(model)
    # pprint.pprint(table.all())