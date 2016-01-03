# -*- coding: utf-8 -*-
import os


def main():
    os.system('cls')
    print 'Welcom Windows Installer'
    print '  ** NOTICE:'
    print '       1.check your disk is *MBR*.'
    print '       2.check your disk is free.\n'

    # Read File
    IMG_Floor='IMG_File'
    for dirPath, dirNames, fileNames in os.walk(IMG_Floor):
        print dirPath,'(Floor)'
    ImgFile=[]
    for i in xrange(0,len(fileNames)):
        if '.esd' in fileNames[i] or '.wim' in fileNames[i]:
            ImgFile.append(fileNames[i])
    for i in xrange(0,len(ImgFile)):
        print ('  [%d]--%s'%(i,ImgFile[i]))


    # Chose File
    FileNum = int(raw_input("\n>>> Chose FileNum: "))
    Install_File= \
        'Dism /Get-Wiminfo /WimFile:'+IMG_Floor+'\\'+ \
        ImgFile[FileNum]
    os.system('cls')
    os.system(Install_File)


    # Chose Image Index
    print '========================================'
    print '** Chose Image Index'
    IndexNum = raw_input(">>> Chose IndexNum: ")


    # Chose Disk
    os.system('cls')
    os.system('fsutil fsinfo drives')
    print '========================================\n'
    print '** Chose your disk:'
    print '     code only. EX: e or E \n'
    DiskCode = raw_input(">>> Chose disk: ")

    
    # Finaly Check
    os.system('cls')
    print '**Finaly Check**'
    print '========================================'
    print 'File   =',ImgFile[FileNum]
    print 'Image  =',IndexNum
    print 'Disk   =',DiskCode
    print '========================================'
    print '** if information is wrong.'
    print '** you can press [CTRL+C] or [n] restart.\n'
    print '  ** NOTICE:'
    print '     1.check your disk is *MBR*.'
    print '     2.check your disk is free.\n'
    print '** Now copy file to disk.'
    print '** It need a long time.\n'
    Copy_File='Dism /apply-image /imagefile:'+ \
        IMG_Floor+'\\'+ImgFile[FileNum]+ \
        ' /index:'+IndexNum+ \
        ' /applydir:'+DiskCode+':\\'
    

    # Cpoy File
    Final_Check = raw_input(">>> yes or no : ")
    if Final_Check=='Y' or Final_Check=='y' or \
        Final_Check=='yes'or Final_Check=='YES':
        # print Copy_File
        os.system(Copy_File)
    else:
        return


    # BDC rebuild
    BCD_Build= \
        'bcdboot.exe ' +\
        DiskCode+':\windows /f ALL /s '+DiskCode+':\\'
    # print BCD_Build
    os.system(BCD_Build)


    # Finish
    # os.system('cls')
    print '\n** Windows is Install success.'
    print '** Now only two step.'
    print '     1.Set partition is Active.'

if __name__ == '__main__':
    main()