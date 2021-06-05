from sqlalchemy import inspect
from sqlalchemy.orm import ColumnProperty

def create_from_resource(cls, resource):
    mapper = inspect(cls)
    kwargs = {}
    for column in mapper.attrs:
        if not isinstance(column, ColumnProperty):
            # skip anything not a plain column
            continue
        
        key = column.key
        value = resource.get(key)
        if value is not None:
            kwargs[key] = value
    return cls(**kwargs)


def update_from_resource(model, resource):
    instance_state = inspect(model)
    for column in instance_state.mapper.attrs:
        if not isinstance(column, ColumnProperty):
            continue
        
        key = column.key
        value = resource.get(key)
        if value is not None:
            setattr(model, key, value)
