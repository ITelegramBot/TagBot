def getUserName(chat):
    username = ""
    if chat.first_name:
        username += chat.first_name
    if chat.last_name:
        username += chat.last_name
    return username