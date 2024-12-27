# Escape sequence character       
# \’	- Single quote       
# \\’ - Double quote         
# \\ - Backslash          
# \n - Newline               
# \r - Carriage Return         
# \t - Horizontal Tab           
# \b - Backspace             
# \f - Formfeed                 
# \v - Vertical Tab             
# \0 - Null Character             
# \N{Name} - Unicode character   Database named lookup              
# \uxxxxxxxx - Unicode character   with a 16-bit hex value          
# \Uxxxxxxxx - Unicode character   with a 32-bit hex value         
# \000 - Character with octal value   ooo                        
# \xhh - Character with hex value    hh  

a = "Harry is a good boy\nbut not a  bad\n \"boy\" "      

print(a)