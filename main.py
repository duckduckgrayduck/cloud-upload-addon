""" We use lootdl, a library to grab files from several file sharing sites
and the DocumentCloud Add-On system"""
import os
import sys
import shutil
from clouddl import grab
from documentcloud.addon import AddOn

class Import(AddOn):
    """An Add-On that allows you to upload files into DocumentCloud from
    Google Drive, Dropbox, Mediafire, and WeTransfer"""

    def main(self):
        """
            Uses clouddl to grab documents from a Google Drive or Dropbox location, 
            uploads them to DocumentCloud using upload_directory()
        """
        os.makedirs(os.path.dirname("./out/"), exist_ok=True)
        stdout = sys.stdout
        # suppress output to prevent leaking private information. 
        sys.stdout = open(os.devnull, "w")
        url = self.data["url"]
        grab(url, "./out/")
        project_id = self.data.get("project_id")
        project = self.client.projects.get(project_id)
        obj_list = self.client.documents.upload_directory("./out/", extensions=None, project=project.id, access=self.data.get("access_level"))
        shutil.rmtree("./out/", ignore_errors=False, onerror=None)
        # restore stdout
        sys.stdout = stdout


if __name__ == "__main__":
    Import().main()
