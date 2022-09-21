import sys
from documentcloud.addon import AddOn
from documentcloud import DocumentCloud
import subprocess

class GDriveImport(AddOn):
	def main(self):
		client = DocumentCloud(#Insert credentials here, redacted for public repository) 
		file = input("Please provide the link of the Google Drive folder or file you'd like to upload to DocumentCloud \n")
		cmd = 'python3 gdrivedl.py -P "out" ' + file   
		
		try:
			retcode = subprocess.call(cmd, shell=True)
			if retcode < 0:
				print("Child was terminated by signal", -retcode, file=sys.stderr)
			else:
				print("Child returned", retcode, file=sys.stderr)
		except OSError as e:
			print("Execution failed:", e, file=sys.stderr)

		title = input('Please provide a project title for the folder you would like to upload to DocumentCloud \n')
		project, created = client.projects.get_or_create_by_title(title)
		obj_list = client.documents.upload_directory('/home/s/gdrivedl/out/')
		project.document_list = obj_list
		project.put()

if __name__ == "__main__":
    GDriveImport().main()
