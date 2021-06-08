import dropbox
import os
class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(file_to, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        
        with open(file_to, "rb") as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode("overwrite"))
    
def main():
    accessToken = "sl.AyADaRseJbFsrAGfwp1bBLqnGvnrPHLAqtqVn3xCdakY0EpxK9PWMI3Ka5BpJKtNiaibWtVLrSPk0AZ9z2Dexs26bYKfGweaRVGlcoiM9KHOJGxITZY7hUYkpns3qI2v08p4Ep3SqQsJ"
    transferData = TransferData(accessToken)

    fileFrom = input("Enter the file to upload to Dropbox:")
    fileTo = input("Enter the destination path of the Dropbox:")

    transferData.upload_file(fileFrom, fileTo)

if __name__ == "__main__":
    main()