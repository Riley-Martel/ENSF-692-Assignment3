# school_data.py
# Riley Martel
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
import math
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here
#EnrollmentData is the variable used to store all of given_data
enrollmentData = 0
#schoolNameCode is a dictionary containing all schools for given_data and the associated codes
schoolNameCode = {
        "Centennial High School": 1224,
        "Robert Thirsk School": 1679,
        "Louise Dean School": 9626,
        "Queen Elizabeth High School": 9806,
        "Forest Lawn High School": 9813,
        "Crescent Heights High School": 9815,
        "Western Canada High School": 9816,
        "Central Memorial High School": 9823,
        "James Fowler High School": 9825,
        "Ernest Manning High School": 9826,
        "William Aberhart High School": 9829,
        "National Sports School": 9830,
        "Henry Wise Wood High School": 9836,
        "Bowness High School": 9847,
        "Lord Beaverbrook High School": 9850,
        "Jack James High School": 9856,
        "Sir Winston Churchill High School": 9857,
        "Dr. E. P. Scarlett High School": 9858,
        "John G Diefenbaker High School": 9860,
        "Lester B. Pearson High School": 9865
    }
class DataError(ValueError):
    '''Creates a ValueError of type DataError, this is used for input checking'''
    pass
# You may add your own additional classes, functions, variables, etc.
def createDataArray():
    '''createDataArray uses the imported given_data and joins it all together into a numpy array of shape(10,20,3)
    representing the year, school, grade called data. It then returns the numpy array data'''
    data = np.stack((year_2013,year_2014,year_2015,year_2016,year_2017,year_2018,year_2019,year_2020,year_2021,year_2022))
    data = data.reshape(10,20,3)
    return data.copy()


def getInput():
    '''getInput takes user input for either the school name or the school code. It checks if the input is within the 
    global dictionary schoolNameCode and raises the error DataError if it is not in the dictionary. The index of the entered input in
    the dictionary is returned aswell as the name of the school.'''
    error = True
    index = 0
    name = 0
    while error:
        value = input("Please enter the high school name or code: ")    
        try:
            for i,v in enumerate(schoolNameCode):
                if value == v or value == str(schoolNameCode.get(v)):
                    error = False
                    index = i
                    name = v
            if error == True:
                raise DataError("[Inavlid school name or code]")
        except DataError:
                print("You must enter a valid school name or code. Please try again")
                error = True
    return index,name


def main():
    print("ENSF 692 School Enrollment Statistics")
    enrollmentData = createDataArray()
    #fills the enrollmentData with the given_data 
    print("Shape of full data array: " + str(enrollmentData.shape))
    print("Dimensions of full data array: " + str(enrollmentData.ndim))
    # Print Stage 1 requirements here
    # Prompt for user input
    value,school = getInput()
    #Sets value to the index of the user inputed school and sets school to the school
    maskedData = np.ma.masked_where(enrollmentData[:,value,:] < 500, np.nan_to_num(enrollmentData[:,value,:]), copy=True)
    #Creates an array that masks all enrollment values less than 500 and sets all NaN to 0
    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    print("School Name: " + school + ", School Code: " + str(schoolNameCode.get(school)))
    print("Mean enrollment for Grade 10: " + str(math.floor(np.nanmean(enrollmentData[:,value,0]))))
    print("Mean enrollment for Grade 11: " + str(math.floor(np.nanmean(enrollmentData[:,value,1]))))
    print("Mean enrollment for Grade 12: " + str(math.floor(np.nanmean(enrollmentData[:,value,2]))))
    print("Highest erollment for a single grade: " + str(math.floor(np.nanmax(enrollmentData[:,value,:]))))
    print("Lowest erollment for a single grade: " + str(math.floor(np.nanmin(enrollmentData[:,value,:]))))
    print("Total enrollment for 2013: " + str(math.floor(np.nansum(enrollmentData[0,value,:]))))
    print("Total enrollment for 2014: " + str(math.floor(np.nansum(enrollmentData[1,value,:]))))
    print("Total enrollment for 2015: " + str(math.floor(np.nansum(enrollmentData[2,value,:]))))
    print("Total enrollment for 2016: " + str(math.floor(np.nansum(enrollmentData[3,value,:]))))
    print("Total enrollment for 2017: " + str(math.floor(np.nansum(enrollmentData[4,value,:]))))
    print("Total enrollment for 2018: " + str(math.floor(np.nansum(enrollmentData[5,value,:]))))
    print("Total enrollment for 2019: " + str(math.floor(np.nansum(enrollmentData[6,value,:]))))
    print("Total enrollment for 2020: " + str(math.floor(np.nansum(enrollmentData[7,value,:]))))
    print("Total enrollment for 2021: " + str(math.floor(np.nansum(enrollmentData[8,value,:]))))
    print("Total enrollment for 2022: " + str(math.floor(np.nansum(enrollmentData[9,value,:]))))
    print("Total ten year enrollment: " + str(math.floor(np.nansum(enrollmentData[:,value,:]))))
    print("Mean total enrollment over 10 years: " + str(math.floor(np.nansum(enrollmentData[:,value,:])/10)))
    if math.floor(np.ma.amin(maskedData))>500:#checks if there is atleast one enrollment value greater than 500
        print("For all enrollments over 500, the median value was: " + str(math.floor(np.ma.median(maskedData))))
    else:
        print("No enrollments over 500.")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    print("Mean enrollment in 2013: " + str(math.floor(np.nanmean(enrollmentData[0,:,:]))))
    print("Mean enrollment in 2022: " + str(math.floor(np.nanmean(enrollmentData[9,:,:]))))
    print("Total graduating class of 2022: " + str(math.floor(np.nansum(enrollmentData[9,:,2]))))
    print("Highest erollment for a single grade: " + str(math.floor(np.nanmax(enrollmentData[:,:,:]))))
    print("Lowest erollment for a single grade: " + str(math.floor(np.nanmin(enrollmentData[:,:,:]))))


if __name__ == '__main__':
    main()

