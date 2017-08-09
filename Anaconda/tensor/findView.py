# coding=utf-8
import os


def isView(file):
    bhasExtends = False
    bconstruct = False  #
    for line in file:
        if line.find(' extends ') > 0:
            bhasExtends = True
        elif (line.find('super(context, attrs)') >= 0 \
                      or line.find('super(context, attrs, defStyleAttr)') >= 0 \
                      or line.find('super(context, attrs, defStyleAttr)') >= 0):
            bconstruct = True

        if bhasExtends and bconstruct:
            return True

    return bhasExtends and bconstruct


def dirlist(path, allfile):  # (string,list)->list
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if filename.find('.') != 0:
            if os.path.isdir(filepath):
                try:
                    dirlist(filepath, allfile)
                except Exception as e:
                    print('Exception:', e, ' path:', filepath)
            elif (filepath.find('.java') > 0 or filepath.find('.kt') > 0):
                with open(filepath, 'r', encoding='UTF-8') as file:
                    if isView(file):
                        allfile.append(filepath)
    return allfile


projects = "F:\AndroidStudio\ptxProjects"  # 工程列表目录
fileLists = dirlist(projects, [])

for f in fileLists:
    print(f[len(projects) + 1:])
print(len(f))
