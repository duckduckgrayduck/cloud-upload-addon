""" We use lootdl, a library to grab files from several file sharing sites
and the DocumentCloud Add-On system"""
import os
import sys
import shutil
import lootdl
from documentcloud.addon import AddOn

class Import(AddOn):
    """An Add-On that allows you to upload files into DocumentCloud from
    Google Drive, Dropbox, Mediafire, and WeTransfer"""

    def main(self):
        """
        This add-on creates a temporary directory(out),
        gets the URL from the DocumentCloud add-on prompt,
        gets the project name from the DocumentCloud add-on prompt,
        uses the lootdl library's grab() to download the files into ./out/,
        finds the project matching the project name and uploads it to the project.
        If the project doesn't exist, it creates the project and then uploads.
        This is handled by get_or_create_by_title().
        The temporary directory is then deleted.
        """
        os.makedirs(os.path.dirname("./out/"), exist_ok=True)
        stdout = sys.stdout
        # suppress output to prevent leaking private information. 
        sys.stdout = open(os.devnull, "w")
        url = self.data["url"]
        lootdl.grab(url, "./out/")
        project_id = self.data.get("project_id")
        project = self.client.projects.get(project_id)
        obj_list = self.client.documents.upload_directory("./out/", project=project.id, access=self.data.get("access_level"))
        project.document_list = obj_list
        project.put()
        shutil.rmtree("./out/", ignore_errors=False, onerror=None)
        # restore stdout
        sys.stdout = stdout


if __name__ == "__main__":
    Import().main()
