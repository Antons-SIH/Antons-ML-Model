import PreProcessor
import OCR
import AadharExtractor as AE

def getAadharDictionary(path,path2):
    PreProcessor.removeMarathiWordsfromImage(path,path2)
    OCRList=OCR.getOCRList(path)
    Dict=AE.getAadharDict(OCRList)
    return Dict

# use for testing the final code
if __name__ == '__main__':
    Dict= getAadharDictionary("/Users/aditya_gitte/Projects/SIH/Antons-ML-Model/SampleImages/Aadhar/Aryan_new.jpeg","/Users/aditya_gitte/Projects/SIH/Antons-ML-Model/Aadhar/Dump/marathiRemovedImage.jpeg")
    print(Dict)