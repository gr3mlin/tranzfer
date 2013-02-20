# detects presence of SD card
# transfers files to local storage, hashes and logs the hash, keeps track of # of files in transfer que
# make connection with other nodes
# transfers files to other nodes
# checks and deletes files for which the hash has arrived

#this now only works on *Nix

import md5, logging, pickle, os, glob

FILENAME = 'filedirectory.txt'
FILETYPES = ['.gif', '.jpg', '.jpeg', '.mpg', '.mpeg', '.mp4', '.avi']

logging.basicConfig(filename='log.log',level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def checkFileDirectory():
	try:
		directory = open(FILENAME, 'r')
	except:
		logging.warning("creating File Directory")
		directory = open(FILENAME, 'wb')
		directory.close()
	return null

def pickleToFile(info):
	directory = open(FILENAME, 'wb')
	pickle.dump(info, directory)
	directory.close()
	return null

def pickleFromFile():
	directory = open(FILENAME, 'rb')
	return(pickle.load(directory))

#this needs to be refined.. basically useless - need to hash only the results of listFiles()
def hashFiles():
	hashes = []
	for file in os.listdir(os.getcwd()):
		hasher = md5.new()
		try:
			output = open(file, 'r')
			hasher.update(output.read())
			hashes.append(hasher.hexdigest())
		except:
			logging.error("couldn't hash: " + file)
	return hashes

def pollDf():
	mounted = []
	os.system('df > df.txt')
	df = open('df.txt', 'r')
	for line in df.readlines():
		line = line.strip()
		rec = dict(zip(gdf_cols, line.split(None, 5)))
		filesys = rec['filesys']
		dir = rec.get('dir')
		if (dir and not (filesys.find(':') >= 0 or pseudofilesys.get(filesys))):
			mounted.append(dir)
	return mounted

#currently these two functions do not walk directories. they need too

def listFilesDwd(directory):
	listOfFiles = []
	for format in FILETYPES:
		listOfFiles = listOfFiles + (glob.glob(directory + '/*' + format))
	return listOfFiles

#this function is probably not that useful..
def listFiles():
	listOfFiles = []
	directory = os.getcwd()
	for format in FILETYPES:
		listOfFiles = listOfFiles + (glob.glob(directory + '/*' + format))
	return listOfFiles

### MAIN ###

