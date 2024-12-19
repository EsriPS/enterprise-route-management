Instructions for running ERM_GenerateOrderPairs.py

1. Will need to popupate ERM_Plan_Defaults.gdb. Specifically GeoOrderTemplate and DepotTemplate layers.
2. In GeoOrderTemplate, set Depot Name = name of depot you want the order pair created at
3. Open Pro and add ERM_Plan_Defaults layers to map (need GeoOrderTemplate, DepotTemplate layers and OrderPairTemplate table)
4. Open Default toolbox and open ERM_GenerateOrderPairs

Parameters:
Order Layer = GeoOrderTemplate
Depot Layer = DepotTemplate
Write to Same Table = if checked, will add new orders to GeoOrderTemplate. If unchecked, will let user add new name. New feature class created in Pro default workspace.
Dispatch Location Name = name of location orders are for
Suffix = suffix to add to OrderID for new orders created
Stop Type for New Orders = Sets StopType for new orders to Pickup or Delivery. Assumes existing orders are set to the other value.
Order Pairs Table Name = OrderPiarTemplate