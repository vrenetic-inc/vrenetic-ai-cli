from tinydb import TinyDB, Query


__database_table_ann__ = 'ann-models'
__database_table_workflow__ = 'workflow-models'


def getDB():
    return TinyDB(__basepath_db__)


def getANNTable():
    return getDB().table(__database_table_ann__)


def getWorkflowTable():
    return getDB().table(__database_table_workflow__)


def getANNById(id):
    table = getANNTable()
    return findById(table, id)


def getANNAll():
    table = getANNTable()
    return findById(table, '')


def getWorkflowById(id):
    table = getWorkflowTable()
    return findById(table, id)


def getWorkflowAll():
    table = getWorkflowTable()
    return findById(table, '')


def findById(table, id):
    query = Query()
    return table.search(query.id.matches(id))

