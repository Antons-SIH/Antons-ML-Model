import Aadhar.OCR_dictionary as adh
import Pan.PanDict as pan

def getAadharDictionary(path):
    adh.getAadharDictionary(path)

def getPanDictionary(modelPath,weightsPath,dumpPath,imgPath):
    obj=pan.PanDict(modelPath,weightsPath,dumpPath,imgPath)
    dict=obj.getPanDict()
    return dict

#testing
print(getAadharDictionary("/Users/aditya_gitte/Projects/SIH/Antons-ML-Model/SampleImages/Aadhar/pranav.jpeg"))
print(panDict=getPanDictionary("/Users/aditya_gitte/Projects/SIH/Antons-ML-Model/Pan/yolov5","/Users/aditya_gitte/Projects/SIH/Antons-ML-Model/Pan/best.pt","/Users/aditya_gitte/Projects/SIH/Antons-ML-Model/Pan/best.pt","/Users/aditya_gitte/Projects/SIH/Antons-ML-Model/SampleImages/Pan/6.jpeg"))