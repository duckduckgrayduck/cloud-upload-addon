from documentcloud.addon import AddOn
from documentcloud import DocumentCloud
import lootdl
import shutil
import os

""" This add-on creates a temporary directory(out), 
    gets the URL from the DocumentCloud add-on prompt, 
    gets the project name from the DocumentCloud add-on prompt, 
    uses the lootdl library's grab() to download the files from the specified URL into the out directory, 
    finds the project matching the project name and uploads it to the project. 
    If the project doesn't exist, it creates the project and then uploads. 
    This is handled by get_or_create_by_title(). 
    The temporary directory is then deleted.
 """


class Import(AddOn):
    def main(self):
        os.makedirs(os.path.dirname("./out/"), exist_ok=True)
        file = self.data.get("url")
        lootdl.grab(file, "./out/")
        title = self.data.get("projectname")
        project, created = self.client.projects.get_or_create_by_title(title)
        obj_list = self.client.documents.upload_directory("./out/", project=project.id)
        shutil.rmtree("./out/", ignore_errors=False, onerror=None)


if __name__ == "__main__":
    Import().main()
