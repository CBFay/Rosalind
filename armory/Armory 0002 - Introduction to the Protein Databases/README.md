# Introduction to the Protein Databases

## Problem
The UniProt Knowledgebase can be found here:  
http://www.uniprot.org/help/uniprotkb

You can see a complete description of a protein by entering its UniProt access ID into the site's query field. Equivalently, you may simply insert its ID (uniprot_id) directly into a UniProt hyperlink as follows:

http://www.uniprot.org/uniprot/uniprot_id
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Swiss-Prot holds protein data as a structured .txt file. You can obtain it by simply adding .txt to the link:

http://www.uniprot.org/uniprot/uniprot_id.txt
Given: The UniProt ID of a protein.

Return: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).

## Sample Dataset
Q5SLP9
## Sample Output
DNA recombination
DNA repair
DNA replication

### Programming Shortcut
ExPASy databases can be accessed automatically via Biopython’s Bio.ExPASy module. The function .get_sprot_raw will find a target protein by its ID.

We can obtain data from an entry by using the SwissProt module. The read() function will handle one SwissProt record and parse will allow you to read multiple records at a time.

http://rosalind.info/problems/dbpr/

