""" We use lootdl, a library to grab files from several file sharing sites
and the DocumentCloud Add-On system"""
import os
import shutil
from documentcloud.addon import AddOn
import lootdl


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
        url = self.data.get("url")
        lootdl.grab(file, "./out/")
        title = self.data["project_name"]
        project, created = self.client.projects.get_or_create_by_title(title)
        self.client.documents.upload_directory("./out/", project=project.id)
        shutil.rmtree("./out/", ignore_errors=False, onerror=None)


if __name__ == "__main__":
    Import().main()
