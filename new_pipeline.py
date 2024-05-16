
#Load necessary modules
import os
import sys
import glob
import subprocess
from Bio import SeqIO
from Bio import Phylo
from Bio.Seq import Seq

#create string variables to store directories for input and output
direct_in = "/shared/forsythe/BB485/Week06/Brass_CDS_seqs/"
direct_out = "/home/largentl/novus/Assignments/Tutorial_Assignments/Week_6/phylogenomic_pipeline_/new_out/"
#get a list of all files for input
file_names_inp = glob.glob(direct_in+"*fasta")

'''
TESTING: shorten the list
remove command once you want to run all ~9000 fasta files
file_names_inp=file_names_inp[0:15]
'''

#Run through mafft using loop to search through input files and create alignment files
for file in file_names_inp:
    print(file) #to test
    file_path_new = file.replace(direct_in,direct_out)
    print(file_path_new) #to test
    aln_cmd = 'mafft --auto --quiet '+file+' > ' + file_path_new
    print(aln_cmd) #to test
    os.system(aln_cmd)

#makes a list of aligned file names using glob
aln_file_names= glob.glob(direct_out+"*fasta")
print(aln_file_names) #to test

#loop through all alignment files in list of aligned file names and create a tree for each
for aln in aln_file_names:
    tree_command = f"iqtree -s {aln} -m TEST -nt 2"
    print(tree_command)
    os.system(tree_command)

#Step 3: Read in the trees and count given topologies
tree_file_names = glob.glob(direct_out+"*treefile")
print(tree_file_names)

#Create empty list
topology_list=[]

for tree in tree_file_names:
#Read in the tree and store as phylo object
    temp_tree = Phylo.read(tree, "newick")

    #Loop through the tips in the tree to find which one contains Es (the outgroup)
    for tip in temp_tree.get_terminals():
        if "Es_" in tip.name:
            es_tip = tip
            #Stop the loop once correct tree tip is found
            break
    
    #Root tree by outgroup taxon
    temp_tree.root_with_outgroup(es_tip)
    
    #Get a list of all terminal (aka tips) branches
    all_terminal_branches = temp_tree.get_terminals()
    
    #Loop through the branches and store the names of the tips of each
    for t in all_terminal_branches:
        if "Bs_" in t.name:
            Bs_temp=t 
        elif "Cr_" in t.name:
            Cr_temp=t
        elif "At_" in t.name:
            At_temp=t
        else:
            out_temp=t
        
    #Make lists of pairs of branches, so that we can ask which is monophyletic
    P1_and_P2=[Bs_temp, Cr_temp]
    P1_and_P3=[Bs_temp, At_temp]
    P2_and_P3=[Cr_temp, At_temp]
    

    #Use series of if/else statemetns to ask which pair in monophyletic
    if bool(temp_tree.is_monophyletic(P1_and_P2)):
        topo_str = "12top"
    elif bool(temp_tree.is_monophyletic(P1_and_P3)):
        topo_str = "13top"
    elif bool(temp_tree.is_monophyletic(P2_and_P3)):
        topo_str = "23top"
    else:
        topo_str = "Unknown"
    topology_list.append(topo_str)

print(topology_list) #to test

total_12top = topology_list.count("12top")
total_13top = topology_list.count("13top")
total_23top = topology_list.count("23top")

print(f"# of trees with Bs and Cr sister: {total_12top}")
print(f"# of trees with Bs and At sister: {total_13top}")
print(f"# of trees with Cr and At sister: {total_23top}")

#Make a submission script (.sh) to run (put python new_pipeline.py as command for submission script)

#Challenge: create a simple figure that shows the counts