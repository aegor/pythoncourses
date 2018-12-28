from peewee import *
import json
from playhouse.shortcuts import model_to_dict, dict_to_model

def models_to_dict(models):
    return [model_to_dict(c) for c in models]

def tojson(obj):
    return json.dumps(obj, ensure_ascii=False)
