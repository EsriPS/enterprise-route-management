"""
--------------------------------
Name:        ERM_CreateGroups.py
Purpose:     Create Portal groups used by Enterprise Route Management system
Author:      Mike Nelson
Created      5/26/2020
Copyright:   (c) Esri
ArcGIS Version:   2.4 (Pro)
PYTHON Version:   3.6 (API 1.8)
Requirements: update group_list variable.
              Create Environment variables exist for credentials, or just change variables to store directly
--------------------------------
"""

import arcpy, os, sys
from arcgis.gis import GIS
from os import environ

group_list = ["COV", "OCC", "GOL", "INL"]

# portal credentials
erm_portal = environ["ERM_PORTAL"]
erm_user = environ["ERM_USER"]
erm_pswd = environ["ERM_PWD"]

# Sign in/connect to portal
gis = GIS(erm_portal, erm_user, erm_pswd, verify_cert=False)

for group_name in group_list:
    tag_list = f"dispatch-location-{group_name}, ERM"
    arcpy.AddMessage(f"Creating group {group_name}...")
    geocaching_group = gis.groups.create(title=group_name,
                                         tags=tag_list,
                                         description=f"ERM group for location {group_name}",
                                         access='org',
                                         is_invitation_only='False')

