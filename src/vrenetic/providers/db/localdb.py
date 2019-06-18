from tinydb import TinyDB, Query


def getById(id):
    Item = Query()
    db = TinyDB(__basepath_db__)
    table = db.table('ann-models')
    application_config = table.search(Item.id.matches(id))
    return application_config

def getAll():
    Item = Query()
    db = TinyDB(__basepath_db__)
    table = db.table('ann-models')
    application_config = table.search(Item.id.matches(''))
    return application_config


def getWorkflowById(id):
    Item = Query()
    db = TinyDB(__basepath_db__)
    table = db.table('workflow-models')
    workflow_config = table.search(Item.id.matches(id))
    return workflow_config


def getWorkflowAll():
    Item = Query()
    db = TinyDB(__basepath_db__)
    table = db.table('workflow-models')
    application_config = table.search(Item.id.matches(''))
    return application_config

