#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UKKXR602
#
# Created:     09/06/2021
# Copyright:   (c) UKKXR602 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os
import shutil
import datetime

#variables for input table
relationship_tab = arcpy.GetParameterAsText(0)
input_dataset = arcpy.GetParameterAsText(1)
#so this would be input table, you can make a parameter with a multii-input so you could select tables

desc_data = arcpy.Describe(input_dataset)
path_desc = desc_data.path

arcpy.AddMessage ("Table Path = " + str(path_desc))

##just let me know

#Get Origin and Destination FC Names

arcpy.AddMessage("Getting origin/destination fields and feature classes")

feature_name = os.path.basename(relationship_tab).split('\\')[0]
Table_create = input_dataset + "\\" + feature_name

arcpy.AddMessage ("feature name is " + str(feature_name))
arcpy.AddMessage ("Relationship class to be created is " + str(Table_create))

desc = arcpy.Describe(relationship_tab)
arcpy.AddMessage(desc.destinationClassNames)
Origin_Feature = str(desc.originClassNames[0])
arcpy.AddMessage ("origin class is " + Origin_Feature)
Dest_Feature = str(desc.destinationClassNames[0])
arcpy.AddMessage ("dest class is: " + Dest_Feature)
OriginClassKeys = desc.originClassKeys[0]
DestinClassKeys = desc.originClassKeys[1]
Primarykey = OriginClassKeys[0]
Foreignkey = DestinClassKeys[0]
arcpy.AddMessage ("Primary guy for relationship is: " + str(Primarykey))
arcpy.AddMessage ("Foreign key for relationship is: " + str(Foreignkey))
Forward_label = str(desc.forwardPathLabel)
back_label = str(desc.backwardPathLabel)
cardinality = str(desc.cardinality)
relNotif =  str(desc.notification)
rel_compdesc =str(desc.isComposite)
attributed = str(desc.isAttributed)
arcpy.AddMessage ("attributed is " +  attributed)
TEST = desc.destinationClassKeys

arcpy.AddMessage ("Destion keys are : " + str(TEST))

#Read existing relationship to figure out input for cardinality
if cardinality == "OneToOne":
    cardin_input = "ONE_TO_ONE"
if cardinality == "OneToMany":
    cardin_input = "ONE_TO_MANY"
if cardinality == "ManyToMany":
    cardin_input = "MANY_TO_MANY"

arcpy.AddMessage ("Cardinality is " + cardin_input)

#read existing relationship to figure out input for message direction
if relNotif == "None":
    message_dir = "NONE"
if relNotif == "Forward":
    message_dir = "FORWARD"
if relNotif == "Backward":
    message_dir = "BACKWARD"
if relNotif == "Both":
    message_dir = "BOTH"

arcpy.AddMessage ("Message direction is " + message_dir)

#read existing feature to see if dataset is attributed
if attributed == "False":
    input_attribute = "NONE"
if attributed != "False":
    input_attribute = "ATTRIBUTED"

arcpy.AddMessage("Attribution is " + input_attribute)

#read existing feature to see if dataset is composite or simple
if rel_compdesc == "False":
    input_rel_type = "SIMPLE"
if rel_compdesc != "False":
    input_rel_type = "COMPOSITE"

arcpy.AddMessage("Attribution is " + input_attribute)

#calculate final inputs
input_origin = input_dataset + "\\" + Origin_Feature
input_destin = path_desc + "\\" + Dest_Feature
new_relationship_name = input_dataset + "\\" + feature_name


arcpy.management.CreateRelationshipClass(input_origin,input_destin, new_relationship_name,
           input_rel_type, Forward_label, back_label, message_dir, cardin_input,
              input_attribute, Primarykey, Foreignkey)