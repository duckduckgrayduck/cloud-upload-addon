from documentcloud.addon import AddOn
from documentcloud import DocumentCloud
import lootdl
import shutil
import os

class Import(AddOn):
	def main(self):
		os.makedirs(os.path.dirname('./out/'), exist_ok=True)
		file = self.data.get("url")
		lootdl.grab(file, './out/')
		title = self.data.get("pname")
		project, created = self.client.projects.get_or_create_by_title(title)
		obj_list = self.client.documents.upload_directory('./out/', project=project.id)
		shutil.rmtree('./out/', ignore_errors=False, onerror=None)
		
if __name__ == "__main__":
	Import().main()

