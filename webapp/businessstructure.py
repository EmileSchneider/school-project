import pickle


class BusinessStructureHandler:
    def __init__(self):
        self.data = {}
    
    def add(self, key, description):
        if key not in self.data.keys():
            self.data[key] = description

    def remove(self, key):
        if key in self.data.keys():
            self.data[key] = None
            
    def updateKey(self, oldkey, newkey):
        if oldkey in self.data.keys():
            data = self.data[oldkey]
            self.data[newkey] = data
            self.data[oldkey] = None

    def updateDescription(self, key, newDescription):
        if key in self.data.keys():
            self.data[key] = newDescription
        
    def save(self):
        pass
    


class BusinessStructureHandlerMongoDb(BusinessStructureHandler):
    def __init__(self, col):
        self.col = col
        self.ident = 'structure'
        self.data = {}
        self.__loadsavefile__()

    def __loadsavefile__(self):
       if dataobj := self.col.find({'ident': self.ident}) is not None:
           self.data = dataobj

    def save(self):
        self.col.update(self.data)


class BusinessStructureHandlerPickledObject(BusinessStructureHandler):
    def __init__(self):
        self.__saveobjfilepath__ = 'business_structure_save_obj.pkl'
        self.__loadsavefile__()

    def save(self):
        pickle.dump( favorite_color, open(self.__saveobjfilepath__, "wb" ) )
        
    def __loadsavefile__(self):
        try:
            f = open(self.__saveobjfilepath__, 'wb')
            self.data = pickle.load(f)
            f.close()
        except:
            self.data = {}

class BusinessStructureEditorController:

    def __init__(self):
        self.handler = BusinessStructureHandler()

    def add(self, key, description):
        self.handler.add(key, description)

    def remove(self, key):
        self.handler.remove(key)

    def updateKey(self, oldkey, newkey):
        self.handler.updateKey(oldkey, newkey)

    def updateDescription(self, key, newDescription):
        self.handler.updateDescription(key, newDescription)

    def save(self):
        self.handler.save()

    def get_keys_and_descriptions(self):
        return {"message": "the information keys", "data": self.handler.data}
    
    
