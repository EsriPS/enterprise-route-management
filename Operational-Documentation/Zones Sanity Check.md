 **Sanity Quality Check for Route Zones**- [Job Aid](https://en.wiktionary.org/wiki/job_aid)
This job aid uses an ArcGIS Pro notebook to run geometric evaluations of a ZoneTemplate layer and creates a report of zone polygon shapes that would likely cause a VRP solve request to fail. 
1. Create a new project in ArcGIS Pro
2. Add a your ZoneTemplate layer to the map
![Image for Add Zones](https://github.com/rConger/doc_images/blob/main/ZonesLayer.jpg?raw=true)

3. Fron the Insert menu, choose to insert an existing notebook and browse to the location where you downloaded [ZoneChecker.ipynb](https://github.com/EsriPS/enterprise-route-management/commit/cce72a38f3d93997c7b468dfb65115b2ab617a96) to add it to the project

![Image for Add Notebook](https://github.com/rConger/doc_images/blob/main/addNotebook1.jpg?raw=true)

4. From the Notebook folder in the project catalog view, find the notebook and open it
![Image for Open Notebook](https://github.com/rConger/doc_images/blob/main/OpenNotebook.jpg?raw=true)

5. Make any necessary changes to temporary files path or zones layer name, then run the notebook 
![Image for Adjust and Run Notebook](https://github.com/rConger/doc_images/blob/main/AdjustNotebookAndRun.jpg?raw=true)

6. Depending on the number of zones, the notebook may take up to 2 minutes to run. When it's finished, you'll notice run report data in the notebook output an a new table added to the TOC. 
![Image for Run Complete](https://github.com/rConger/doc_images/blob/main/RunReport.jpg?raw=true)

7. Open the new table added and have a look at the attributes. first four columns indicate the quality check that was failed. Records with at least one failed metric will be added to the table. Any given record could fail more than one check. 
![Image for Report Table](https://github.com/rConger/doc_images/blob/main/ReportTable.jpg?raw=true)

The tests corresponding to the columns are:
* **Sliver Polygons** - any feature where perimiter length >= area
* **Excessive Vertices** - any feature whose aveage vertex spacing is closer than 200 meters
* **Interior Voids** - any feature where the number if rings is more than one greater than the number of feature parts
* **Excessive Parts** - any feture with more than 4 discontigous parts (e.g. islands)

8. You can join the report table to the original Zones polygon layer on failedZoneCheck.Source OBJECTID -> ZoneTemplate.OBJECTID to more easily examine any failed feature. For example:   
![Image for Failed Check](https://github.com/rConger/doc_images/blob/main/FailedCheck1.jpg?raw=true)
![Image for Failed Check](https://github.com/rConger/doc_images/blob/main/FailedCheck2.jpg?raw=true)
