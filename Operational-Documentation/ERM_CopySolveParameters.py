import arcpy


def get_value_list(in_layer, field_name):
    with arcpy.da.SearchCursor(in_layer, [field_name]) as cursor:
        return sorted({row[0] for row in cursor})

################### UPDATE VARIABLES ##############################
depot_template = r"C:\ERM\services\fgdbs\ERM_Plan_Defaults.gdb\DepotTemplate"
depot_name_field = "depotname"
solve_param_defaults_table = r"C:\ERM\services\fgdbs\ERM_Solve_Parameters.gdb\Solve_Parameters_Restrictions_DefaultValues"
solve_param_table = r"C:\ERM\services\fgdbs\ERM_Solve_Parameters.gdb\Solve_Parameters_Restrictions"
solve_para_depot_field = "displocname"

# make view for tables for selection/calculate tools to use
solve_param_view = "solve_param_view"
arcpy.MakeTableView_management(solve_param_table, solve_param_view)

# get list of all depot locations
depot_list = get_value_list(depot_template, depot_name_field)

for depot in depot_list:
    arcpy.AddMessage(f"Processing {depot}...")

    arcpy.AddMessage("Append default records...")
    arcpy.Append_management(solve_param_defaults_table, solve_param_table, "NO_TEST")
    arcpy.AddMessage("Select blank records...")
    arcpy.management.SelectLayerByAttribute(solve_param_view, "NEW_SELECTION", solve_para_depot_field + " = ''", None)
    arcpy.AddMessage("Calculate depot name...")
    arcpy.management.CalculateField(solve_param_view, solve_para_depot_field, f"'{depot}'", "PYTHON3", '', "TEXT")
