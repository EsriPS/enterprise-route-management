 **Deleting a Plan** from ERM - [Job Aid](https://en.wiktionary.org/wiki/job_aid)
This job aid uses the Portal UI and ArcGIS Pro to find and delete plans. These tasks could be automated through the [Python API](https://developers.arcgis.com/python/) as well
1. Open the ERM_Registry table in ArcGIS Pro.
2. Search for a plan by the "Dispatch Location", "First Event" (Creation time), "Last Event" (Last updated time), or any of the other fields. Optionaly, set a definition query on any field.
![Image for Pro Query](https://user-images.githubusercontent.com/3834298/90927990-a97aac80-e3bb-11ea-9e40-0c90c28fe903.jpg)
3. Note the "Item Id" which corresponds to Feature Layer ID. The "Webmap Id" which corresponds to the Web Map, and (if applicable), the "Dashboard Id" which corresponds to a plan dashboard if one was created. 
4. In Portal, search for and delete the following items in the following order
* If applicable: the Dashboard
* Webmap item
![Image for delete web map](https://user-images.githubusercontent.com/3834298/90928011-b4cdd800-e3bb-11ea-9c39-65be90843180.jpg)
* Feature layer
* Row for the plan in ERM_Registry

The plan is now completely deleted and will no longer appear in any items inventory including RPE. 
