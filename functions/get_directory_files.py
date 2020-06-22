import __main__ as main

def get_directory_files(directory, search_pattern):
    paths = main.Path(directory).glob(search_pattern)
    files = []
    for path in paths:
        files.append(str(path))
    return files