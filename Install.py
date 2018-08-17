# # Prerequisites :
# # 1. Check version of pip: It should be 9.3.0
import sys, os,json
import pip
class Script:

	def __init__(self):
		self.dicdata={}
		self.dictF={}


#  retriving data from the .json file
	def getData(self,name):
		f=open(name,'r')
		data=json.load(f);
		self.dicdata=data.get("Dependencies")
		f.close()

#  Install the dependencies mentioned in the json file
	def getJsonDependenciesInstalled(self):
		for key,val in self.dicdata.items():
			if os.system("pip install"+" "+str(key)+"=="+str(val))==0:
				print(str(key)+"=="+str(val)+" installed successfully")
			elif os.system("pip install"+" "+str(key)+"=="+str(val))==1:
				self.dictF[key]=val;
				print(str(key)+"=="+str(val)+" installation Failed")
				

#  Failed Installations
	
	def failedInstallation(self):
		return self.dict3

if __name__ == '__main__':
	obj=Script()

	# Method to get data from .json file
	obj.getData("Dependencies.json")

	# Method to install the dependencies mentioned in .json file
	dictt=obj.getJsonDependenciesInstalled()
	if dictt=={}:
		print "Success"
	else:
		print "Fail"

	
	


	

































