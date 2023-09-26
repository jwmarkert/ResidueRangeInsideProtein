from Bio import SeqIO
from Bio import ExPASy
import requests
import xml.etree.ElementTree as ET

residues = str(input("Enter the residues you are interested in: "))

uniprot_id = str(input("Enter the protein uniprot ID (if you want to use a sequence, put 0): "))

if uniprot_id == '0':
    print("Enter the protein sequence (type an empty line to finish input):")
    protein_name_lines = []
    while True:
        line = input()
        if not line:
            break
        protein_name_lines.append(line)
    
    # Join the collected lines into a single string
    protein = ''.join(protein_name_lines)
else:
    # Fetch the sequence from UniProt using ExPASy
    try:
        with ExPASy.get_sprot_raw(uniprot_id) as handle:
            record = SeqIO.read(handle, "swiss")
            protein = str(record.seq)
    except Exception as e:
        print(f"Error fetching sequence: {str(e)}")
        protein = None

def get_protein_name(uniprot_id):
    base_url = "https://www.uniprot.org/uniprot/"
    url = f"{base_url}{uniprot_id}.xml"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the XML response to extract the protein name
            root = ET.fromstring(response.text)
            protein_name = None
            for entry in root.findall(".//{http://uniprot.org/uniprot}entry"):
                protein_name = entry.find("{http://uniprot.org/uniprot}name").text
                break  # We only need the first entry
            return protein_name
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {str(e)}")
        return None

if uniprot_id == '0':
    protein_name = str(input("Enter the protein name: "))
else:
    protein_name = get_protein_name(uniprot_id)

substring = residues

def find_all_positions(main_string, substring):
    positions = []
    start = 0
    while True:
        start = main_string.find(substring, start)
        if start == -1:
            break
        end = start + len(substring) - 1
        positions.append((start, end))
        start += 1
    return positions

positions = find_all_positions(protein, substring) 

def add_1_to_tuples(positions):
    Location = []
    for tpl in positions:
        modified_tpl = tuple(val + 1 for val in tpl)
        Location.append(modified_tpl)
    return Location

Location = add_1_to_tuples(positions)

print(f"Your residues are in the range {Location} for the protein {protein_name}")
