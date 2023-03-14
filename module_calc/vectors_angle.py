import module_calc.calculator_specific_functions as csf
import module_calc.numeric_string_parser_class as nspc
import numpy as np


DD_OR_DMS= "DMS"

def dd_to_dms(dd):
   is_positive = dd >= 0
   dd = abs(dd)
   minutes,seconds = divmod(dd*3600,60)
   degrees,minutes = divmod(minutes,60)
   degrees = degrees if is_positive else -degrees
   return [degrees,minutes,seconds]


def angle_between_vectors(vector_x_parsed, vector_y_parsed):
    vector_x_normalized = csf.normalize_vector(vector_x_parsed.array)
    vector_y_normalized = csf.normalize_vector(vector_y_parsed.array)
    result = np.arccos(np.clip(np.dot(vector_x_normalized[0], vector_y_normalized[0]), -1.0, 1.0))
    if csf.DEG_OR_RAD == "DEG":
        if DD_OR_DMS == "DD":
            final_result = result * (180 / np.pi)
        if DD_OR_DMS == "DMS":
            dmsresult = dd_to_dms(result* (180 / np.pi))
            final_result = str(dmsresult[0])+"° "+str(dmsresult[1])+"\' "+str(dmsresult[2])+"\'\'"
    if csf.DEG_OR_RAD == "RAD":
        final_result = result
    return ("The angle between the vectors is "+str(final_result))