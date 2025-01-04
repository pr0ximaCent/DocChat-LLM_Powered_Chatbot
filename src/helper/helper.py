import os
import toml
import shutil

class Helper:
    def createFile(self, file):
        fileLocation = f"temp/{file.name}"
        temp_dir = "temp"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        fileLocation = f"{temp_dir}/{file.name}"
        with open(fileLocation, "wb+") as fileObject:
            fileObject.write(file.getbuffer())

@@ -12,15 +16,6 @@ def createFile(self, file):
    def deleteFile(self, filePath):
        os.remove(filePath)

    # def set_api_key(self,google_api_key):
    #     with open(".streamlit/secrets.toml", "r+") as f:
    #         secrets = toml.load(f)
    #         secrets["palm_api_key"] = google_api_key
    #         f.seek(0)
    #         toml.dump(secrets, f)
    #         f.truncate()
    #     return True
    def set_api_key(self, api_key_name, api_key_value):
        with open(".streamlit/secrets.toml", "r+") as f:
            secrets = toml.load(f)
@@ -29,3 +24,4 @@ def set_api_key(self, api_key_name, api_key_value):
            toml.dump(secrets, f)
            f.truncate()
        return True