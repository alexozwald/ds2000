"""
@author:    Alex Oswald + Thy Nguyen
@class:     DS2001
@created:   17 November 2021

Attributes:
    BACMET_metal (str): filename
    CARD_antibiotic (str): filename
"""
import csv

BACMET_metal = "datafiles/BacMet2_EXP.753.mapping.txt"
CARD_antibiotic = "datafiles/card-genomes.txt"

'''
 - BACMET_metal data structure - 
row[0] = BacMet_ID, ID #
row[1] = Gene_name, gene name
row[2] = Accession, ???
row[3] = Organism, bacterium identifier (genus + species)
row[4] = Location, of gene
row[5] = Compound, list of resive metal compounds

 - CARD_antibiotic data structure - 
row[0] = dna_accession, ID # ???
row[1] = pathogen, bacterium identifier (genus + species)
row[2] = data_source, location of gene
row[3] = perfect_hits, gene lists
row[4] = strict_hits, ???
row[5] = drug_classes, list of classifications of resistive antibiotics
'''

'''
 - Processed data_bacmet Data Structure -
row[0], str:        gene
row[1], List[str]:  perfect_hits (bacterium)
row[2], List[str]:  metals

 - Processed data_card Data Structure -
row[0], str:        name
row[1], List[str]:  gene list
row[2], List[str]:  affected classes
'''


def import_bacmet():
    """imports and cleans data from TSVs
    
    Returns:
        TYPE: desc
    """
    data_bacmet = []
    with open(BACMET_metal, 'r') as f0:
        reader = csv.reader(f0, delimiter='\t')
        next(reader) # skip header

        for row in reader:
            row_list = []
            #row_list.append(row[0])  # don't import BACMET ID -> we don't care
            row_list.append(row[1])   # gene -> can be subsets of gene separated by /s -> still one gene
            #row_list.append(row[2])  # ***unknown use*** -> so we don't care
            row_list.append(row[3])   # one name, long string
            # list of resistances
            metals_raw = row[5].split(', ')
            metals = metal_list_refine(metals_raw)
            row_list.append(metals)

            data_bacmet.append(row_list)

    # data_bacmet list filled
    return data_bacmet


def import_card():
    """Summary
    """
    data_card = []
    with open(CARD_antibiotic, 'r') as f1:
        reader = csv.reader(f1, delimiter='\t')
        header = next(reader)

        for row in reader:
            row_list = []
            # add bacterium name (incl special cases)
            if len(row[0]) > 20:
                #print(f"{len(row[0])}, {row[0]}")
                partial_id = row[0].split("-")[-1]
                bacterium_name = str(row[1] + "-" + partial_id)
                row_list.append(bacterium_name)
            else:
                row_list.append(row[1].lower())


            gene_list = row[3].split(',')
            gene_list = [x.strip() for x in gene_list]
            #gene_list = [x.lower() for x in gene_list]
            # decided to leave case in tact for genes!
            row_list.append(gene_list)
            affected_classes = row[5].split(';')
            affected_classes = [y.lower().strip() for y in affected_classes]
            row_list.append(affected_classes)
            data_card.append(row_list)

    # card data list filled
    return data_card


# METALS CONVERSION DICTIONARY
metals_dict = {
    "Aluminium (Al)": 'Al',
    "Antimony (Sb)": 'Sb',
    "Arsenic (As)": 'As',
    "Bismuth (Bi)": 'Bi',
    "Cadmium (Cd)": 'Cd',
    "Chromium (Cr)": 'Cr',
    "Cobalt (Co)": 'Co',        # occurs 2x
    "Cobalt (Cobalt)": 'Co',    # occurs 2x
    "Copper (Cu)": 'Cu',
    "Gallium (Ga)": 'Ga',
    "Gold (Au)": 'Au',
    "Iron (Fe)": 'Fe',
    "Lead (Pb)": 'Pb',
    "Magnesium (Mg)": 'Mg',
    "Manganese (Mn)": 'Mn',
    "Mercury (Hg)": 'Hg',
    "Molybdenum (Mo)": 'Mo',
    "Nickel (Ni)": 'Ni',
    "Selenium (Se)": 'Se',
    "Silver (Ag)": 'Ag',
    "Tellurium (Te)": 'Te',
    "Tungsten (W)": 'W',
    "Vanadium (V)": 'V',
    "Zinc (Zn)": 'Zn',
}

def metal_list_refine(raw_list):
    # init new list
    refined_list = []

    # run whole list and make comparisons
    for x in raw_list:
        x.strip()
        # if metal + parentheses...
        if (x.title() in metals_dict.keys()):
            refined_list.append(metals_dict[x])
        elif ("[class:" in x):
            #print(x.split('[')[0].strip().lower())
            refined_list.append(x.split('[')[0].strip().lower())
        elif x != "":   # does not occur, but for safety
            #print(x.lower().strip('.'))
            refined_list.append(x.lower().strip('.'))

    return refined_list


# test staging

def _test(x=5):
    data_bacmet = import_bacmet()
    data_card = import_card()
    
    from pprint import pp
    pp(data_bacmet[0:x], indent=4, compact=True)
    print()
    pp(data_card[0:x], indent=4, compact=True)

    pass


if __name__ == '__main__':
    _test()
