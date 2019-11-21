class cd:
    def __init__(self, directory):
        self.directory = directory

    def __enter__(self):
        self.start_dir = os.getcwd()
