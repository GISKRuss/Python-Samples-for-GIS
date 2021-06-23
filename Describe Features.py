#-------------------------------------------------------------------------------
# Name:        Summarise GDD
# Purpose:     Script breaks down feature classes within a GDD and provides
#              report in CSV format. Used for looking into new schemas
# Author:      Kane Russell
#
# Created:     05/12/2018
# Copyright:   (c) UKKXR602 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv
import arcpy
import datetime

#Date
now = datetime.datetime.now()
Date = now.strftime("%Y%m%d")

csvLocation = arcpy.GetParameterAsText(0)
arcpy.env.workspace = arcpy.GetParameterAsText(1)

csv_output = csvLocation + "\\" + "GDD_Summary_" + str(Date) + ".csv"

#write header                                                                                                             ;
with open(csv_output,'wb') as openCSV:
    a = csv.writer(openCSV)
    message = [['FC','NAME', 'TYPE', 'LENGTH', 'NULL']]
    a.writerows(message)

    #Get list of feature classes in geodatabase
    FCs = arcpy.ListFeatureClasses()

    #Loop through feature classes in list
    for FC in FCs:
        #List fields in feature class
        fields = arcpy.ListFields(FC)

        #Loop through fields and write to csv
        for field in fields:

            message = [[FC, field.name, field.type, field.length, field.isNullable]]
            a.writerows(message)