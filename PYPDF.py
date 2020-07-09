from tabula import read_pdf
import tabula
import os
list=["22-1789-20.pdf","22-1796-15.pdf","22-1797-17-EN.pdf","22-1799-23A-EN.pdf","22-1807-11A-EN.pdf","22-1808-16A-EN.pdf","22-1815-13A-EN.pdf","22-1899-1H-EN.pdf","22-1900-1H-EN.pdf","22-1901-1J-EN.pdf","22-1910-1D-EN.pdf","22-1912-1C-EN.pdf","22-1913-1D-EN.pdf","22-1914-1C-EN.pdf"]
# csv=["22-1789-20.csv","22-1796-15.csv","22-1797-17-EN.csv","22-1799-23A-EN.csv","22-1807-11A-EN.csv","22-1808-16A-EN.csv","22-1815-13A-EN.csv","22-1899-1H-EN.csv","22-1900-1H-EN.csv","22-1901-1J-EN.csv","22-1910-1D-EN.csv","22-1912-1C-EN.csv","22-1913-1D-EN.csv","22-1914-1C-EN.csv"]
# pages=["5,6,7","5,6,7","5,6,7,8","5,6,7,8","5,6,7,8","5,6,7,8,9,10","5,6","7,8,9,10","7,8,9","8,9,10,11,12","6,7,8,9","7,8,9","4,5,6,7","5,6"]

csv=["22-1789-20-kit-kit.csv","22-1796-15-kit.csv","22-1797-17-EN-kit.csv","22-1799-23A-EN-kit.csv","22-1807-11A-EN-kit.csv","22-1808-16A-EN-kit.csv","22-1815-13A-EN-kit.csv","22-1899-1H-EN-kit.csv","22-1900-1H-EN-kit.csv","22-1901-1J-EN-kit.csv","22-1910-1D-EN-kit.csv","22-1912-1C-EN-kit.csv","22-1913-1D-EN-kit.csv"]
pages=["4","4","4","4","4","4","4","5,6","5,6","6,7","5","6","3"]

# list=["RT-PRC023AR-EN_01142019.pdf","RT-PRC048L-EN_01142019.pdf","RT-PRC053F-EN_01142019.pdf","PKGP-PRC013T-EN_02092019.pdf","RT-PRC078E-EN_06082019.pdf"]
# csv=["RT-PRC023AR-EN_01142019.csv","RT-PRC048L-EN_01142019.csv","RT-PRC053F-EN_01142019.csv","PKGP-PRC013T-EN_02092019.csv","RT-PRC078E-EN_06082019.csv"]
# pages=["5,6,7,30,31,36,37,38,39","26,27","25,26,29,30","4,5,23,24,26,27,29,30","17,18"]

i=0
j=0
k=0

print(len(list))
print(len(csv))
print(len(pages))
for i in range(0,len(list)+1):

    for k in range(0,len(pages)+1):
        d1 = read_pdf(list[i], pages=pages[k])
        for j in range(0,len(csv)+1):
            tabula.convert_into(list[i], csv[j], output_format="csv", pages=pages[k])
            print(list[i])
            print(csv[j])
            print(pages[k])
            i=i+1
            j=j+1
            k=k+1


# d1=read_pdf("22-1789-20.pdf", pages=[5,6,7])
# d2=read_pdf("22-1797-17-EN.pdf", pages=[5,6,7,8])
# d3=read_pdf("22-1796-15.pdf", pages=[5,6,7])
#
#
# # tabula.convert_into('22-1789-20.pdf',"22-1789-20.csv",output_format="csv",pages=[5,6,7])
# tabula.convert_into('22-1808-16A-EN.pdf',"22-1808-16A-EN.csv",output_format="csv",pages=[5,6,7,8,9,10])


