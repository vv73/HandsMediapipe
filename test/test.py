import os
def getAllPics(dir_name):
    dir_path = '.'
    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(os.path.join(dir_path, path))
    return res


