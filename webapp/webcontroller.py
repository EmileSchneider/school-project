class MainPageController:
    def __init__(self, businesshandler):
        self.businesshandler = businesshandler

    def get_data(self):
        retlist = []
        for res in self.businesshandler.get_10_newest_entries():
            if res:
                retlist.append(res['name'])
        return {"message": "10 latest inserts:", "data": retlist}
    
