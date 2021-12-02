import os
import sys

import xlrd
from xlutils.copy import copy
import datetime


def main(rootdir='原文件夹', resdir='现文件夹', renamefile='批量命名文件.xls'):
    """
        1. 原文件位置 rootdir = '原文件夹'
        2. 现文件位置 resdir ='现文件夹'
        3. 批量命名文件 renamefile = '批量命名文件.xls'
    """

    execl_file = xlrd.open_workbook(renamefile)
    sheet = execl_file.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    excel = copy(execl_file)
    table = excel.get_sheet(0)

    # 从第2行开始处理，直到最后一行
    for i in range(1, nrows):
        # 原文件名称，在第1列
        ori_name = sheet.cell(i, 0).value + '.pdf'
        ori_name = os.path.join(rootdir, ori_name)
        # 修改之后的名称，在第2列
        res_name = sheet.cell(i, 1).value + '.pdf'
        res_name = os.path.join(resdir, res_name)

        # 用os模块中的rename方法对文件进行改名
        os.rename(ori_name, res_name)
        print("已修改 {} 为 {}".format(ori_name, res_name))


if __name__ == '__main__':
    # main(sys.argv[1], int(sys.argv[2]))
    main()
    print("Finish")
