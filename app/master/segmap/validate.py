

def validate_update(model):
    model.pop('dt_create') 

    return model