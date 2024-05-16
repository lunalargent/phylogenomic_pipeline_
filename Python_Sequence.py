#!/usr/bin/python3
#Import needed modules

import pandas as pd

# Create a string object that is a full path to a tsv file
file_path = "/shared/forsythe/BB485/Week05/A_thaliana_chr5_genes_table_short.tsv"

# Read the tsv file in as a dataframe
annot_df = pd.read_csv(file_path, delimiter= "\t")

# Print the dataframe to get a look at it
print(annot_df)

#Get the full path to the DNA sequence
seq_file_path = "/shared/forsythe/BB485/Week05/A_thaliana_chr5_short.fa"

seq_file_handle = open(seq_file_path, "r")

#Create an empty dictionary
seq_dict = {}

#Loop through the line in the file
for line in seq_file_handle:
    if line.startswith(">"):
        id_temp = line.strip() #Removes "\n"
        id_clean = id_temp.replace(">", "") #Removes ">" by replacing with nothing.
        
        #Add the item to the dictionary
        seq_dict[id_clean]="" # id_clean is the key, the value is an empty string (for now)
    else:
        seq_line = line.strip() #Removes "\n"
        
        #append this line to the dictionary value, using the key (which is still "id_clean" from the previous line)
        seq_dict[id_clean] += seq_line

print(seq_dict["Chr5"][0:100]) 

#Loop through the rows of the dataframe
for i in annot_df.index:
    
    if annot_df.iloc[i]['type'] == "gene":

        #Get the type of feature
        temp_type = annot_df.iloc[i]['type']
        
        #Get the start position
        temp_start = annot_df.iloc[i]['start']

        #Get the stop position
        temp_stop = annot_df.iloc[i]['end']

        #Create a print statement
        print(f"Type:{temp_type},Start:{temp_start},End:{temp_stop}")
        print(seq_dict["Chr5"][temp_start:temp_stop])

# Read in the DNA sequence associated with the annotations
