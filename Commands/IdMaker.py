tid = 0


def get_id():
    global tid
    current_id = tid
    tid += 1
    return current_id
