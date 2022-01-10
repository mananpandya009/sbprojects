def convert_temp(unit_in, unit_out, temp):
  """Convert farenheit <-> celsius and return results.

  - unit_in: either "f" or "c" 
  - unit_out: either "f" or "c"
  - temp: temperature (in f or c, depending on unit_in)

  Return results of conversion, if any.

  If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

  For example:

  convert_temp("c", "f", 0)  =>  32.0
  convert_temp("f", "c", 212) => 100.0
  """
  if unit_in == "c" and unit_out == "f":
    converted_temp = (temp * (9/5)) + 32
    return f"should be {converted_temp}"

  elif unit_in == "f" and unit_out == "c":
    converted_temp = (temp - 32) * (5/9)
    return f"should be {converted_temp}" 

  elif unit_out == unit_in:
    return f"should be {temp}"

  elif unit_in != "c" and unit_in != "f":
    return f"should be invalid unit in {unit_in}"

  elif unit_out != "c" and unit_out != "f":
      return f"should be invalid unit out {unit_out}"



print(convert_temp("c", "z", 0))
print(convert_temp("z", "c", 212))
