from flask import Flask, jsonify, request, abort
from . import databaselayer as db

from . import businessstructure  as bs
BusinessStructureEditorController = bs.BusinessStructureEditorController


from .webcontroller import MainPageController
app = Flask(__name__)

DatabaseLayer = db.DatabaseLayer
dbl = DatabaseLayer()
mpc = MainPageController(dbl.new_business_handler())

@app.route('/main')
def main():    
    data = mpc.get_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({"message": "No Businesses in the database"})
    

bsec = BusinessStructureEditorController()
@app.route('/editstructure', methods = ['POST', 'GET', 'PUT', 'DELETE'])
def editstructure():
    if request.method == 'POST':
        # post expects a type:json request with {"key": thekey, "description": thebloodydescription}
        if not request.json:
            abort(400)
        else:
            key = request.json['key']
            desc = request.json['description']
            if not key == "" and not desc  == "":
                bsec.add(key, desc)
                bsec.save()
            else:
                abort(400)
            return jsonify(sucess=True)
        
    if request.method == 'GET':
        return bsec.get_keys_and_descriptions()

    if request.method == 'PUT':
        # put wants json {"typetoupdate": 'key' or 'description',
        #   key Update    'key': theoldkey, 'newkey': thenewkey}
        # descirption: 'key': theKEY, 'description': newdescription
        print(request.json)
        if not request.json:
            abort(400)
        typetoupdate = request.json['typetoupdate']
        if typetoupdate == 'key':
            bsec.updateKey(request.json['oldkey'], request.json['newkey'])
            bsec.save()
            return jsonify(success=True)
        if typetoupdate == 'description':
            bsec.updateDescription(request.json['key'], request.json['description'])
            bsec.save()
            return jsonify(success=True)
        else:
            abort(400)

    if request.method == 'DELETE':
        # expects {'key': theKeytoDelete}
        if not request.json:
            abort(400)
        key = request.json['key']
        bsec.remove(key)
        bsec.save()
        return jsonify(sucess=True)
