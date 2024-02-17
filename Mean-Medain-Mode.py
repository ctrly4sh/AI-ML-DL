#Mean using numpy in python
def Mean(DATA):
    import numpy as np
    meanResult = np.mean(DATA)
    return meanResult

DATA_set = [99,86,87,88,111,86,103,87,94,78,77,85,86]
resultMean = Mean(DATA_set)
# print(resultMean)

 

DATA_set = [99,86,87,88,111,86,103,87,94,78,77,85,86]
resultMedeain = Median(DATA_set) 
# print(resultMedeain)


# Median using numpy in python
def Mode(DATA):
    from scipy import stats # install scipy using pip , numpy doesnt have a function for mode  
    modeResult = stats.mode(DATA)
    return modeResult

DATA_set = [99,99,99,99,99,86,87,88,111,86,103,87,94,78,77,85,86]
resultMode = Mode(DATA_set)
# print(resultMode)



