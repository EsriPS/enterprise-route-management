 **Deleting a Plan** from ERM - [Job Aid](https://en.wiktionary.org/wiki/job_aid)
This job aid uses the Portal UI and ArcGIS Pro to find and delete plans. These tasks could be automated through the [Python API](https://developers.arcgis.com/python/) as well
1. Open the ERM_Registry table in ArcGIS Pro.
2. Search for a plan by the "Dispatch Location", "First Event" (Creation time), "Last Event" (Last updated time), or any of the other fields. Optionaly, set a definition query on any field.
![Image for Pro Query](https://user-images.githubusercontent.com/3834298/90927990-a97aac80-e3bb-11ea-9e40-0c90c28fe903.jpg)
3. Note the "Item Id" which corresponds to Feature Layer ID. The "Webmap Id" which corresponds to the Web Map, and (if applicable), the "Dashboard Id" which corresponds to a plan dashboard if one was created. 

*Note: If you are using the **Workforce Extension for ERM**, save the "Item ID" somewhere you can paste it later if you also need to clear the Workforce project.*

4. In Portal, search for and delete the following items in the following order
* If applicable: the Dashboard
* Webmap item
![Image for delete web map](https://user-images.githubusercontent.com/3834298/90928011-b4cdd800-e3bb-11ea-9c39-65be90843180.jpg)
* Feature layer
* Row for the plan in ERM_Registry

The plan is now completely deleted and will no longer appear in any items inventory including RPE. 

If you are using the **Workforce Extension for ERM**, follow Steps 5-7 below to delete records published into Workforce from ERM 

*Note: This process is not needed for cleaning out older (prior days) features since those features will be purged on a schedule. This process is intended to truncate an active plan so that it can be replaced by a new plan.*

5. Retrive the ItemID you noted in Step 3 above.
6. Generate a token using the steps below
  * a. Go to https://<server name>/portal/sharing/rest/generateToken. <server name> represents the fully qualified domain name of the server that portal is deployed on.
  * b. Enter Username and Password. Use Portal credentials for an administrator level account.
  * c. For Webapp URL, enter the Portal URL. This should match the config.portalUrl value in the Middleware API config file.
![Image for generate token](https://user-images.githubusercontent.com/3834298/94065006-211f6b00-fdb0-11ea-9b81-90c254e36db9.png)

7. Paste  https://<middleware server name>/ermapi/workforce/deletePlan?planItemId=XXX&token=YYY into your browser. <middleware server name> represents the fully qualified domain name of the server that Middleware API is deployed on.
  * Replace XXX with the plan ID previously identified.
  * Replace YYY with the token that was generated.
