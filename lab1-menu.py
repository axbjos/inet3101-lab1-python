################################
#
# Program Name: Parts Record Manager
#
# Author: Joe Axberg
#
################################
import sys

def addRecord():

    print("Adding Part Record\n")

    partNum = int(input("Enter Part Number: "))
    partName = input("Enter Part Name: ")
    partSize = float(input("Enter Part Size: "))
    partSizeMetric = input("Enter Part Size Metric (ex: lbs, kg, inches): ")
    partCost = float(input("Enter Part Cost: "))

    partsDict = { "partNum": partNum, 
                  "partName": partName,
                  "partSize": partSize,
                  "partSizeMetric": partSizeMetric,
                  "partCost": partCost }
    
    print(partsDict)
    
    return partsDict

def printRecords(partsRecordList):

    print("\n\n")
    print("Print out list of parts in database: \n\n")

    for record in partsRecordList:
        print("Part Number: ", record["partNum"])
        print("Part Name: ", record["partName"])
        print("Part Size: ", record["partSize"])
        print("Part Metric: ", record["partSizeMetric"])
        print("Part Cost: ", record["partCost"])
        print("\n\n")

def main():

    # going to put the list of records (aka database) here
    partsRecordList = [];

    # put some data in the list for testing
    partsRecordList.append({"partNum":1, "partName": "wheel", "partSize": 15, "partSizeMetric": "inches", "partCost": 150})
   
    while True:
        print("\nParts Management System\n")
        print("1. Print all records")
        print("2. Add record")
        print("3. Delete the last record")
        print("4. Print number of records")
        print("5. Print database size")
        print("6. Print number of changes")
        print("7. Exit")

        selection = int(input("\nPlease enter your selection (1-7): "))

        #Python doesn't have a traditional case statement

        if selection == 1:

            printRecords(partsRecordList)

        elif selection == 2:

            recordToAdd = addRecord()
            partsRecordList.append(recordToAdd)

        
        elif selection == 4:

            print("\n\nNumber of parts records is: ", len(partsRecordList))

        elif selection == 5:

            print("\n\nSize of parts record database is: ", sys.getsizeof(partsRecordList))


        elif selection == 7:

            print("\n\nThank you for using the Parts Management System")

            #break the loop
            break

main()