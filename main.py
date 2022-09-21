import sys
from documentcloud.addon import AddOn
from documentcloud import DocumentCloud
import subprocess

class GDriveImport(AddOn):
	def main(self):
		file = input("Please provide the link of the Google Drive folder or file you'd like to upload to DocumentCloud \n")
		gdrivedl.main(file)
		title = input('Please provide a project title for the folder you would like to upload to DocumentCloud \n')
		project, created = self.client.projects.get_or_create_by_title(title)
		obj_list = self.client.documents.upload_directory('/home/s/gdrivedl/out/')
		project.document_list = obj_list
		project.put()

if __name__ == "__main__":
    GDriveImport().main()
