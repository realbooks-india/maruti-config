def validate_create(model):

    if not 'dt_create' in model:
        raise Exception("Creation Date is mandatory, not provided!")

    if model['dt_create'] == '' :
        raise Exception("Creation Date is mandatory, cannot be blank!")

    return model


def validate_update(model):

    if 'version' in model:
        model.pop('version') 

    if 'dt_create' in model:
        model.pop('dt_create') 

    return model