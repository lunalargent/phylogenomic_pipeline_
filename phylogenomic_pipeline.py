#Python script for my pipeline

#Pipeline Core Steps and/or Processes

'''
1. acquire a fasta file containing gene family sequences 
and make accessible in computing environment.
2. Run multiple sequence alignment using the mafft command on the command line using
the following format to allow for output to be saved to a file..

mafft [<name-of-gene-family-sequences-file>] [<output-file-name]

3. once multiple sequence alignment is complete, the output file can be used to run a maximum
likelihood algorithm for making inferences for phylogeny with the raxml command as follows...

raxmlHPC-PTHREADS-SSE3 -s <alignment-output-file-name> -n <output-name> -m PROTGAMMALGF -p 12345 -x 12345 -f a -# 100 -T 12

command must be placed and ran within a job submission script 

4. once ran, a file starting with RAxML_bipartitions will appear in the given folder. This file contains the most likely tree from the given
MSA file, and can be viewing by running the following command...

nw_display <newick-formatted-file-name>

5. In order to create a high-quality figure displaying the tree, a python
script can be written following the example format below...

from Bio import Phylo
import matplotlib.pyplot as plt

# Read the Newick file into a tree object
newick_file = "RAxML_bipartitions.<given-name>"
tree = Phylo.read(newick_file, 'newick')

# Root the tree by the taxon "Arabidopsis_thaliana_ATP_synthase_subunit_C_family_protein"
root_taxon = "Plasmodium_falciparum_C0H4L0"
tree.root_with_outgroup({'name': root_taxon})

# Set up figure and axis
fig, ax = plt.subplots(figsize=(30, 20))

# Plot the tree without X and Y axis
Phylo.draw(tree, axes=ax)
ax.set_xticks([])
ax.set_yticks([])

# Remove the box around the outside of the tree
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Save the plot as a PDF
output_pdf = "OUTPUT_phylogenetic_tree.pdf"
plt.savefig(output_pdf)

6. To further analyze the tree's topology, the Phylo program through Biopython can be used, such as
with tree.find_elements(comments=<>), which allows for the find of clades including specific elements.
'''