import os
import shutil
def RunProject(GenAdr1,DirAdrList1):

    adr = GenAdr1
    liDir  = os.listdir(adr)
    Files = {
                'Video':[],
                'Audio':[],
                'Images' :[] ,
                'Code': [],
                'Documents':[],
                'Folders':[],
                }
    extension = {
        "VidExt":(".mp4",".mkv",".avi",'.webm','.flv','.vob','.ogv','.ogg','.wmv','.mpg','.mpeg','.m4v','.3gp','.svi','.m4p'),
        "AudExt":(".mp3",".wav",".opus",".atrac",'.m4a','.aac'),
        "ImgExt":(".jpeg",".png",".jpg",".raw",'.tif','.tiff','.bmp','gif','eps','cr2','.nef'),
        "CodeExt":(".py",'.json',".c",'.pyd',".cpp",".java",'asm','.class','.cmd','.h','.html','.hxx','.jar','.css','.swf','.htm','.xhtml','.jhtml','.jsp','.jspx','.wss','.do','.action','.js','.php','.php3','.php4','.phtml','.rb','rhtml','.shtml','.dll'),
        "DocsExt":(".pdf",'.zip','.xml','.PDF',".txt",'.doc','.docx','.xls','.xlsx','.ppt','.pptx','.ods','.odt','.epub','.exe','.rar')
    }
    try:
        liDir.remove(os.path.realpath(__file__)[-15:])
    except:
        pass
    for fiN in liDir:
        if fiN.endswith(extension["VidExt"]):
            Files["Video"].append(fiN)
        elif fiN.endswith(extension["AudExt"]):
            Files["Audio"].append(fiN)
        elif fiN.endswith(extension["ImgExt"]):
            Files["Images"].append(fiN)
        elif fiN.endswith(extension["CodeExt"]):
            Files["Code"].append(fiN)
        elif fiN.endswith(extension["DocsExt"]):
            Files["Documents"].append(fiN)

        elif os.path.isdir(adr+'\\'+fiN) and (fiN!='AutomaticSortedFiles'):
            Files["Folders"].append(fiN)

    if(os.path.exists(adr)):
        pass
    else:
        os.makedirs(adr)
        
    for i in DirAdrList1.values():
        if(os.path.exists(i)):
            pass
        else:
            os.makedirs(i)

    for key,value in Files.items():
        for i in value:
            shutil.move(adr+'\\'+i,DirAdrList1[key])

    for i in DirAdrList1.values():
        try:
            os.rmdir(i)
        except:
            pass