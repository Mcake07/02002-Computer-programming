is_student = True
campus = "Lyngby"

is_dtu_lyngby_student = (is_student == True) and (campus.lower() == "lyngby")

print(is_dtu_lyngby_student)