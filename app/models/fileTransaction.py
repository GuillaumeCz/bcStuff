class FileTransaction:
    def __init__(self, path):
        self.fileIn = open(path, 'r')
        self.path = path
        self.fileContent = self.fileIn.read()

    def display_content(self):
        print self.fileContent
