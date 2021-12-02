# Rename_files
利用xls文件批量修改文件的命名并进行移动

## 代码用法  
通过修改rootdir, resdir以及renamefile参数来实现效果，如果`resdir == rootdir`，则直接在原文件夹下进行修改，并不会产生移动。  

`def main(rootdir=r'原文件夹', resdir=r'现文件夹', renamefile=r'批量命名文件.xls'):`   
    `"""`  
        `1. 原文件位置 rootdir = '原文件夹'`  
        `2. 现文件位置 resdir ='现文件夹'`  
        `3. 批量命名文件 renamefile = '批量命名文件.xls'`  
    `"""`      
