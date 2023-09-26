# ResidueRangeInsideProtein
Identifies the residue range of an amino acid sequence within a specified protein
This is particularly helpful if you have a snapgene file where you make a truncation/deletion on a protein that either has an N-terminal tag or N-terminal truncation that disrupts the residue numbers (ie: if you have a 6x HIS tag in front, snapgene will say Methionine 1 is actually Methionine 7).

You might need to download a few packages with git (biopython, requests, elementpath)

You need your amino acid sequence of region of interest (ie: region you deleted) and either the uniprot ID of the protein or the actual protein sequence

To run, simply type python <path to ResidueRangeInsideProtein.py>

You will be first prompted to paste your amino acid sequence of region of interest
Next you will be asked to put the uniprot ID (if you do not know, put 0)
If you put 0 for uniprot ID, you will be asked for the actual protein sequence and then the protein name

It will then tell you what residue range your sequence is in
