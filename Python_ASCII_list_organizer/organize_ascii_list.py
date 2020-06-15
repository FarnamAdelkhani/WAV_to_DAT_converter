# -*- coding: utf-8 -*-
"""
Organize a single column list of floating point values into a specified number of columns
"""

import os



def organize_input_dat(input, output_temp):
    
    #Overwrite if file exists
    open(output, 'w+').close()
    
    #Remove leading and trailing whitespace
    single_column_input = []
    
    with open(input, 'r') as input_:
        for line in input_:
            temp = line.strip()
            single_column_input += [temp]
            
            if len(single_column_input) == 12:
                #Store as comma seperated string
                input_row = '%s' % ', '.join(map(str, single_column_input))
                single_column_input = []
                
                with open(output_temp, 'a') as output_:
                    print(input_row, file=output_)
        
        
        #Check for remaining ASCII values            
        if single_column_input:
            input_row = '%s' % ', '.join(map(str, single_column_input))
            
            with open(output_temp, 'a') as output_:
                    print(single_column_input, file=output_)
                
""" Append a comma to end of each column in the output file """
def append_comma(output_temp, output):
   
    open(output, 'w+').close()
    
    with open(output_temp, 'r') as read_column:
        with open(output, 'w') as write_column:
            for row in read_column:
                row = row.rstrip('\n') + ', '
                print(row, file=write_column)
                
if __name__ == "__main__":
    
    """Specify input filename:"""
    input ='violin_sample_44KHz.dat'
    
    #temp output to store values without appended comma
    output_temp ='temporary.dat'
    
    """Specify output filename:"""  
    output = input.replace('.dat','') + '_organized.dat'
    
    #Organize and append
    organize_input_dat(input, output_temp)
    append_comma(output_temp, output)
    
    #Delete temp storage file
    os.remove("temporary.dat")