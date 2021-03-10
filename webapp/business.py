class BusinessHandler:
    def __init__(self, collection):
        self.col = collection

    def get_10_newest_entries(self):
        return self.col.find().sort('_id', -1)[:10]
      
