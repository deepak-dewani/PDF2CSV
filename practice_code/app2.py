# import csv
# import os

# # folder_name = os.mkdir('f3')
# with open('/home/deepak/Documents/pdf2image/f3/page_1.txt', 'r') as file:
#     stripped = (line.strip() for line in file)
#     lines = (line.split(",") for line in stripped)
#     with open('/home/deepak/Documents/pdf2image/f3/page_1.csv', 'w') as out_file:
#         writer = csv.writer(out_file, dialect=csv.excel)
#         writer.writerow(('page no', 'text'))
#         writer.writerow(lines)
#         out_file.write('\n')


# import pandas as pd
# import glob

# file_name = glob.glob("/home/deepak/Documents/pdf2image/f2/*.txt")

# with open('output_file.txt', 'w') as out_file:
#     for i in file_name:
#         with open(i) as in_file:
#             for j in in_file:
#                 out_file.write(j)

# data = pd.read_csv("output.txt", delimiter = '/')
  
# data.to_csv("convert_sample.csv", index = None)


# import csv
# import glob

# column_names = ['text','pageno']


# with open("convert_sample.csv", 'w') as target:
#     writer = csv.DictWriter(target, fieldnames=column_names)
#     writer.writeheader() # if you want a header
#     for path in glob.glob("/home/deepak/Documents/pdf2image/f2/*.txt"):
#         with open(path) as source:
#             reader = csv.DictReader(source, delimiter='/', fieldnames=column_names)
#             writer.writerows(reader)

# import csv
# import itertools

# with open('/home/deepak/Documents/pdf2image/f3/page_1.txt', 'r') as in_file:
#     lines = in_file.read().splitlines()
#     stripped = [line.replace(","," ").split() for line in lines]
#     grouped = itertools.izip(*[stripped]*1)
#     with open('log.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerow(('title', 'intro', 'tagline'))
#         for group in grouped:
#             writer.writerows(group)

# import csv
# import zlib

# with open('/home/deepak/Documents/pdf2image/f3/page_1.txt', 'r') as in_file:
#     lines = in_file.read()
#     print(lines, '\n')
#     stripped = [line.replace(","," ") for line in lines]
#     print(stripped, '\n')
#     joinn = ''.join(stripped)
#     print(joinn)
    # grouped = zip(*[joinn]*1)
    # grouped = str(list(grouped))
    # print(list(grouped), '\n')

    # for i in grouped:
    #     print(i)
    # with open('teste.csv', 'w') as out_file:
    #     writer = csv.writer(out_file)
    # #     print(writer)
    #     writer.writerow(('A'))
    # #     print(writer)

    #     for group in grouped:
    #         writer.writerow(group)

# with open('teste.csv','w') as file:
#     for line in joinn:
#         file.writelines(line)
#         file.write('')
    


# with open('/home/deepak/Documents/pdf2image/f3/page_1.txt', 'r') as infile, open('/home/deepak/Documents/pdf2image/f3/page_1.csv', 'w') as outfile:
#         stripped = (line.strip() for line in infile)
#         lines = (line.split(",") for line in stripped if line)
#         writer = csv.writer(outfile, delimiter= )
#         writer.writerows(lines)

# import csv

# with open('/home/deepak/Documents/pdf2image/f3/page_1.txt', 'r') as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line.split(",") for line in stripped )
#     lines = (',').join(lines)
#     with open('log.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerow(('title', 'intro'))
#         writer.writerows(lines)

# import pandas as pd
# # dataframe_1 = pd.read_csv("/home/deepak/Documents/pdf2image/f3/page_1.txt", sep='\t', lineterminator='\r')
# # dataframe_1.to_csv("/home/deepak/Documents/pdf2image/f3/page_1.csv")


# import glob

# for path in glob.glob("/home/deepak/Documents/pdf2image/f2_text/*.txt"):
#     with open(path) as source:
#         dataframe_1 = []
#         dataframe_1 = pd.read_csv.("/home/deepak/Documents/pdf2image/f2_text/*.txt", sep='\t', lineterminator='\r')
#         dataframe_1.append()
#         dataframe_1.to_csv("/home/deepak/Documents/pdf2image/f3/.csv")

import glob 
import pandas as pd

files = sorted(glob.glob('/home/deepak/Documents/pdf2image/f2_text/*.txt'))
print(files)
dfs = []
print(dfs)
for file in files:
    df = pd.read_csv(file, sep='\t', lineterminator='\r')
    dfs.append(df)
    print(dfs)
# df = pd.concat(dfs).to_csv('/home/deepak/Documents/pdf2image/f3/file.csv')

