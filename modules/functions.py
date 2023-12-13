FILEPATH = "files/tasks.tsk"


def getTodos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items\n
    --------- ---------------------------------------------------------------\n
    'filepath'      the base path to the file and default value is "FILEPATH """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def writeTodos(todos, filepath=FILEPATH):
    """ Write the to-do items list in the text file\n
    --------- ---------------------------------------------------------------\n
    'filepath'      the base path to the file and default value is "FILEPATH"\n
    'todos' - list of to-do items """

    with open(filepath, "w") as file:
        file.writelines(todos)
