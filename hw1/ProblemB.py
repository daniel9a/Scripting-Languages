import os

#read the first n bytes of a file
def readNBytes(fileName,nBytes):
	toRead = open(fileName, 'rb')
	byte = toRead.read(nBytes)

	return byte


#get all files located in this directory and their paths
def fileList(dir_name):
	f = []
        #use os.walk to create file names for 
        for root, dirs, files in os.walk(dir_name, True):
                for name in files:
                        f.append(os.path.join(root, name))
        return f



#takes a dict, returns tuples of len 2 for all values sharing the same key.
def makeTupleList(Data):
	return_val = []

	for key in Data:
		if len(Data[key]) > 1:
			for i in range(len(Data[key])):
				for j in range(1,len(Data[key]) - i):
					return_val.append((Data[key][i], Data[key][i+j]))
	return return_val	


#takes a file name and number of bytes and returns a tuple of any same files.
def filePairs(dir_name, nBytes):
	
	Data = {}

	#getting the names of all the files
	files = fileList(dir_name)

	for f in files:

		#append to list if one does
		if readNBytes(f,nBytes) in Data:
			Data[readNBytes(f,nBytes)].append(f)

		#create list for key if one doesn't exist
		else:
			Data[readNBytes(f,nBytes)] = [f]


	return makeTupleList(Data)
