import os, glob, shutil

#flatting 

currentPath = os.getcwd()

shutil.rmtree(currentPath+'/openapi/flatversion')

os.mkdir(currentPath+'/openapi/flatversion')
os.mkdir(currentPath+'/openapi/flatversion/daysync')
os.mkdir(currentPath+'/openapi/flatversion/common')




paths = [[currentPath+'/openapi/noflatversion/common',currentPath+'/openapi/flatversion/common'],
         [currentPath+'/openapi/noflatversion',currentPath+'/openapi/flatversion'],
         [currentPath+'/openapi/noflatversion/daysync',currentPath+'/openapi/flatversion/daysync']]


for path in paths:
    pathCommon = path[0]
    pathOutput = path[1]

    os.chdir(pathCommon)

    commonFileList = glob.glob('*.yaml')

    for nameFile in commonFileList:
        file = open(nameFile,'r').read()

        start = 0

        while True:
            start = file.find('$ref: \'',start+1)    
            if start == -1:
                break
            end = file.find('\'',start+7)

            nSpace = start - file.rfind('\n',0,start) - 1 
            cSpace = ''
            for i in range(nSpace):
                cSpace = cSpace + ' '

            if file[start+7] != '#':
                nameFileToInclude = file[start+7:end]

                if os.path.exists(currentPath+'/openapi/flatversion'+nameFileToInclude[1:len(nameFileToInclude)]) == True:
                   nameFileToInclude = currentPath+'/openapi/flatversion'+nameFileToInclude[1:len(nameFileToInclude)]

                fileToInclude = open(nameFileToInclude,'r').read()

                file = file.replace(file[start:end+1],fileToInclude.replace('\n','\n'+cSpace))

                start = start - end + len(fileToInclude)  

        open(pathOutput+'/'+nameFile, 'w').write(file)

shutil.rmtree(currentPath+'/openapi/flatversion/common')

