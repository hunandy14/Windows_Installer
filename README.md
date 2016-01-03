# Windows 如何安裝在隨身硬碟上
<br>
如何安裝至隨身硬碟手動步驟可以參考doc文檔<br>
會這麼麻煩主要是因為微軟的安裝程序本身<br>
不允許將windwos安裝在行動裝置<br>
只能透過手動打指令的方式啟動<br>
<br>
建議執行前先在windwos上做好磁碟分割，並注意使用MBR格式<br>
大致就三行指令<br>
查看：Dism /Get-Wiminfo /WimFile:D:\install.esd<br>
安裝：Dism /apply-image /imagefile:D:\install.wim /index:4 /applydir:K:\<br>
安裝BDC：bcdboot K:\windows /f ALL /s K:\<br>
<br>
詳細的介紹可以參考doc文檔<br>
<br>
執行完最後一步設定啟動可以用第三軟體、diskpart指令、或者Windows內建的管理<br>
推薦只用第三種，直接在我的電腦按右鍵管理，找到分區設置成啟動即可<br>
<br>
<br>
基於每次都要打一堆指令實在很麻煩，還要更改磁碟曹有好幾處<br>
用python寫了一個腳本，讓他自動執行，但並沒有很完善，以後再慢慢改<br>
<br>
使用方法：<br>
  1.裝好python2.7<br>
  2.複製所需安裝的wim或esd檔案到IMG_File資料夾內<br>
  3.使用管理開啟CMD(命令提示字元)<br>
  4.切換到該目錄直接執行檔案即可<br>
<br>
<br>
<br>
<br>
<br>
Windows 7 8 10 隨身硬碟 安裝 指令<br>
