 **Deleting a Plan** from ERM - [Job Aid](https://en.wiktionary.org/wiki/job_aid)
This job aid uses the Portal UI and ArcGIS Pro to find and delete plans. These tasks could be automated through the [Python API](https://developers.arcgis.com/python/) as well
1. Use the Search, Sort, and View settings in the Content listing to find the plan you wish to delete. Note that *wildcard* searches are not supported.
![Image for find plan](https://user-images.githubusercontent.com/3834298/90923061-a29b6c00-e3b2-11ea-91ae-e948bae645d9.jpg)
2. Click the item to show its properties and find the item ID for the web map
![Image for get Web map Item ID](https://user-images.githubusercontent.com/3834298/90927963-9ec01780-e3bb-11ea-8fa7-d6a227b2c66b.jpg)
3. Open the ERM_Registry table in ArcGIS Pro and set a definition query for the Webmap id to the item id from Step 2.
![Image for Pro query](https://user-images.githubusercontent.com/3834298/90927990-a97aac80-e3bb-11ea-9e40-0c90c28fe903.jpg)
4. Note the "Item Id" which corresponds to Feature Layer ID
5. If applicable, note the "Dashboard Id"
6. In the following order: search for and delete
* If applicable: the Dashboard
* Webmap item
![Image for delete web map](https://user-images.githubusercontent.com/3834298/90928011-b4cdd800-e3bb-11ea-9c39-65be90843180.jpg)
* Feature layer
* Row for the plan in ERM_Registry
