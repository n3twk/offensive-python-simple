from PyPDF2 import PdfFileReader
import argparse
def printmetadata(fileName):
    pdfFile = PdfFileReader(open(fileName,'rb'))
    docinfo = pdfFile.getDocumentInfo()
    print("[ * ] Printing Metadata for file: " + str(fileName))
    for metaItem in docinfo:
        print("[ + ]" + metaItem + docinfo[metaItem] )


def main():
    parser = argparse.ArgumentParser(prog='pdfmeta.py',usage=' -F filename')
    parser.add_argument('-F', '--filename',help="PDF file")
    args =parser.parse_args()
    filename = args.filename
    if filename == None:
        print(parser.prog + ' ' +parser.usage)
    else:
        print(parser.prog)
        printmetadata(filename)
if __name__ == '__main__':
    main()