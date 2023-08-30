import os, glob, shutil

#setting 
# IMPORTANT: the first folder must be common
currentPath = os.getcwd()
rootFlatted = currentPath+'/openapi/flatversion'
paths = [[currentPath+'/openapi/noflatversion/common',rootFlatted+'/common'],
         [currentPath+'/openapi/noflatversion',rootFlatted],
         [currentPath+'/openapi/noflatversion/daysync',rootFlatted+'/daysync']]

#reset file system
if os.path.exists(rootFlatted) == True:
    shutil.rmtree(rootFlatted)

os.makedirs(rootFlatted)

for path in paths:
    if os.path.exists(path[1]) == False:
        os.mkdir(path[1])                       

#flatting
for path in paths:
    pathCommon = path[0]
    pathOutput = path[1]
    os.chdir(pathCommon)
    commonFileList = glob.glob('*.yaml')

    #flatting single yaml
    for nameFile in commonFileList:
        file = open(nameFile,'r').read()

        #scanning single yaml
        start = 0
        while True:

            #find $ref
            start = file.find('$ref: \'',start+1)    
            if start == -1:
                break
            end = file.find('\'',start+7)

            #setting indentation
            nSpace = start - file.rfind('\n',0,start) - 1 
            cSpace = ''
            for i in range(nSpace):
                cSpace = cSpace + ' '

            
            if file[start+7] != '#':
                nameFileToInclude = file[start+7:end]

                #fetch common flatted
                if os.path.exists(rootFlatted+nameFileToInclude[1:len(nameFileToInclude)]) == True:
                   nameFileToInclude = rootFlatted+nameFileToInclude[1:len(nameFileToInclude)]

                #replace $ref with external file
                fileToInclude = open(nameFileToInclude,'r').read()
                file = file.replace(file[start:end+1],fileToInclude.replace('\n','\n'+cSpace))
                start = start - end + len(fileToInclude)  

        open(pathOutput+'/'+nameFile, 'w').write(file)

#remove common folder
shutil.rmtree(rootFlatted+'/common')

