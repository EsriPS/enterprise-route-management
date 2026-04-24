import arcpy
import sys
from os import path

SHAPE_INDEX = 1
ORDERID_INDEX = 13
DEPOTNAME_INDEX = 27
DISPLOCNAME_INDEX = 28
STOPTYPE_INDEX = 45

# Add current dir to path
tool_dir = path.dirname(path.abspath(__file__))
sys.path.append(tool_dir)

geodatabase = r"C:\Users\jer11410\OneDrive - Esri\Documents\Engagements\ERM\Pro Project\ERM_Plan_Defaults.gdb"
arcpy.env.workspace = geodatabase
arcpy.env.overwriteOutput = True

def printDictionary(d, indent = 0):

    for key, value in d.items():
        arcpy.AddMessage('\t' * indent + str(key))
        if isinstance(value, dict):
            printDictionary(value, indent + 1)
        else:
            arcpy.AddMessage('\t' * (indent + 1) + str(value))

    return

def getDepotLocations(depots):

    depot_fields = []
    for f in arcpy.ListFields(depots):
        depot_fields.append(f.name)

    depot_dict = {}
    with arcpy.da.SearchCursor(depots, depot_fields) as cursor:
        for row in cursor:
            this_dict = {}
            for ii, field_name in enumerate(depot_fields):
                this_dict[field_name] = row[ii]

            #arcpy.AddMessage(f"depot: {row[0]}")
            depot_dict[row[depot_fields.index('displocname')]] = this_dict

    return depot_dict

def main(orders, depots, write_to_same_table, new_orders, location, suf, stop_type, order_pairs):
    
    depot_dict = getDepotLocations(depots)
    #printDictionary(depot_dict)

    order_fields = []
    for f in arcpy.ListFields(orders):
        order_fields.append(f.name)

    #for i, f in enumerate(order_fields):
    #    arcpy.AddMessage(f"{i}: {f}")

    order_pair_fields = []
    for f in arcpy.ListFields(order_pairs):
        order_pair_fields.append(f.name)

    # only get the orders that match the given dispatch location
    order_where_clause = f"displocname = '{location}'"
    #arcpy.AddMessage(f"order_where_clause: {order_where_clause}")

    max_objectid = 0
    with arcpy.da.SearchCursor(orders, 'OBJECTID') as scursor:
        max_objectid = max(max(scursor))
    arcpy.AddMessage(f"max objectid: {max_objectid}")

    with arcpy.da.SearchCursor(orders, order_fields, order_where_clause) as scursor:
        for row in scursor:
            #arcpy.AddMessage(f"orderid: {row[ORDERID_INDEX]}")

            if write_to_same_table and row[0] > max_objectid:
                arcpy.AddMessage("I'm writing to the same table, and I've come to the end or the original orders. Bailing out.")
                break

            op_orderid = row[ORDERID_INDEX] + suf
            op_shape = depot_dict[row[DISPLOCNAME_INDEX]]['shape']
            first_order_name = row[ORDERID_INDEX]
            second_order_name = op_orderid
            #depot = depot_dict[row[DISPLOCNAMEINDEX]]

            original_row = list(row)
            new_row = list(row)
            new_row[SHAPE_INDEX] = op_shape
            new_row[ORDERID_INDEX] = op_orderid
            new_row[STOPTYPE_INDEX] = new_stop_type
            
            if write_to_same_table:    
                # write to the original table
                with arcpy.da.InsertCursor(orders, order_fields) as icursor:
                    icursor.insertRow(new_row)
            else:
                with arcpy.da.InsertCursor(new_orders, order_fields) as icursor:        
                    # First just make a copy of the existing order
                    icursor.insertRow(original_row)

                    # Next make a new row with the delivery attributes
                    icursor.insertRow(new_row)

            # populate the order pair table
            with arcpy.da.InsertCursor(order_pairs_table_name, order_pair_fields[1:]) as opcursor:
                op_new_row = []
                #op_new_row.append(None)                 # OBJECTID
                op_new_row.append(first_order_name)     # First Order Name
                op_new_row.append(second_order_name)    # Second Order Name
                op_new_row.append(None)                 # Max Transit Time
                op_new_row.append(location)             # Dispatch Location
                op_new_row.append(None)                 # Dispatch Description
                op_new_row.append(None)                 # Created By
                op_new_row.append(None)                 # First Event
                op_new_row.append(None)                 # Last Updated By
                op_new_row.append(None)                 # Last Event
                opcursor.insertRow(op_new_row)

    return

if __name__ == "__main__":

    order_layer = arcpy.GetParameterAsText(0) or "TestOrders"
    depot_layer = arcpy.GetParameterAsText(1) or "DepotTemplate"
    write_to_same_table = arcpy.GetParameter(2) or False
    new_order_layer_name = arcpy.GetParameterAsText(3) or "New_" + order_layer
    dispatch_location_name = arcpy.GetParameterAsText(4) or "ADU"
    suffix = arcpy.GetParameterAsText(5) or "_OP"
    new_stop_type = arcpy.GetParameterAsText(6) or "Delivery"
    order_pairs_table_name = arcpy.GetParameterAsText(7) or "TestOrderPair"
    
    arcpy.AddMessage(f"order_layer: {order_layer}")
    arcpy.AddMessage(f"depot_layer: {depot_layer}")
    arcpy.AddMessage(f"write_to_same_table: {write_to_same_table}")
    arcpy.AddMessage(f"new_order_layer_name: {new_order_layer_name}")
    arcpy.AddMessage(f"dispatch_location_name: {dispatch_location_name}")
    arcpy.AddMessage(f"suffix: {suffix}")
    arcpy.AddMessage(f"new_stop_type: {new_stop_type}")
    arcpy.AddMessage(f"order_pairs_table_name: {order_pairs_table_name}")
    
    if not write_to_same_table and new_order_layer_name == '':
        arcpy.AddError(f"ERROR: you have specified to write the results to a separate table, but have not identified the table using the 'New Order Layer Name' parameter.")
        exit()
    
    # if the name given for the new order layer doesn't exist, create it.
    if not arcpy.Exists(new_order_layer_name):
        arcpy.conversion.ExportFeatures(order_layer, new_order_layer_name)
        arcpy.management.DeleteRows(new_order_layer_name)  

    arcpy.AddMessage(f"entering main...")
    main(order_layer, depot_layer, write_to_same_table, new_order_layer_name, dispatch_location_name, suffix, new_stop_type, order_pairs_table_name)