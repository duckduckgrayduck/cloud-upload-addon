from documentcloud.addon import AddOn
from documentcloud import DocumentCloud
import gdrivedl	
class GDriveImport(AddOn):
	def main(self):
		file = self.data.get("url") #input("URL \n")
		gdrivedl.main(file)
		title = self.data.get("projectname") #input("Title \n") for local testing
		project, created = self.client.projects.get_or_create_by_title(title)
		obj_list = self.client.documents.upload_directory('./out/')
		project.document_list = obj_list
		project.put()
if __name__ == "__main__":
    GDriveImport().main()
