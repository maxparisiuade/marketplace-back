import uuid

def generate_short_unique_id():
    unique_id = str(uuid.uuid4().int)[:10]
    return unique_id