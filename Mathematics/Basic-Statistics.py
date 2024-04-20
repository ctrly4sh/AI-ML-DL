#Mean using numpy in python
def Mean(DATA):
    import numpy as np
    meanResult = np.mean(DATA)
    return meanResult

DATA_set = [99,86,87,88,111,86,103,87,94,78,77,85,86]
resultMean = Mean(DATA_set)
# print(resultMean)

def Median(DATA):
    import numpy as np
    meanResult = np.median(DATA)
    return meanResult

DATA_set = [99,86,87,88,111,86,103,87,94,78,77,85,86]
resultMedeain = Median(DATA_set) 
print(resultMedeain)


# Median using numpy in python
def Mode(DATA):
    from scipy import stats 
    modeResult = stats.mode(DATA)
    return modeResult

DATA_set = [99,99,99,99,99,86,87,88,111,86,103,87,94,78,77,85,86]
resultMode = Mode(DATA_set)
# print(resultMode)

#Standard Deviation

def StandardDeviation(DATA):
    import numpy as np
    devaition = np.std(DATA)
    return devaition

speed = [86,87,88,86,87,85,86]
resultDeviation = StandardDeviation(speed)
print(resultDeviation)






