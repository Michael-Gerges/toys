import requests
import pandas as pd
import numpy as np


seq = "TGGTTGTTGTCATTAGCTGTATCGTGAATGACGATATA"

complementry_seq = ""
for letter in seq:
    if letter.lower() == "A".lower():
        complementry_seq += "T"
    elif letter.lower() == "T".lower():
        complementry_seq += "A" 
    elif letter.lower() == "C".lower():
        complementry_seq += "G"
    elif letter.lower() == "G".lower():
        complementry_seq += "C" 


print(complementry_seq)


# convert inchi to inchi key
def inchi_key_trials():
    from chembl_webresource_client.unichem import unichem_client as unichem

    ret = unichem.inchiFromKey('AAOVKJBEBIDNHE-UHFFFAOYSA-N')
    ret = unichem.inchiFromKey('VNPOLUPOVRPMIP-HXUWFJFHSA-N')
    inchi =  ret[0]['standardinchi']



    host = "http://www.chemspider.com"
    getstring = "/InChI.asmx/InChIToInChIKey?inchi="
    #inchi = 'InChI=1S/C6H14N2O2/c7-4-2-1-3-5(8)6(9)10/h5H,1-4,7-8H2,(H,9,10)/t5-/m0/s1'

    r = requests.get('{}{}{}'.format(host, getstring, inchi))
    if r.ok:
      res = str(r.text.replace('<?xml version="1.0" encoding="utf-8"?>\r\n<string xmlns="http://www.chemspider.com/">', '').replace('</string>', '').strip())
    else:
        print ("provide a valid inchi!")

    print(inchi)
    print(res)   




from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski


def lipinski(smiles, verbose=False):

    moldata= []
    for elem in smiles:
        mol=Chem.MolFromSmiles(elem) 
        moldata.append(mol)
       
    baseData= np.arange(1,1)
    i=0  
    for mol in moldata:        
       
        desc_MolWt = Descriptors.MolWt(mol)
        desc_MolLogP = Descriptors.MolLogP(mol)
        desc_NumHDonors = Lipinski.NumHDonors(mol)
        desc_NumHAcceptors = Lipinski.NumHAcceptors(mol)
           
        row = np.array([desc_MolWt,
                        desc_MolLogP,
                        desc_NumHDonors,
                        desc_NumHAcceptors])   
    
        if(i==0):
            baseData=row
        else:
            baseData=np.vstack([baseData, row])
        i=i+1      
    
    columnNames=["MW","LogP","NumHDonors","NumHAcceptors"]   
    descriptors = pd.DataFrame(data=baseData,columns=columnNames)
    
    return descriptors


#df_lipinski = lipinski(df.canonical_smiles)
#print(df_lipinski)

def check_cool_stuff():
    print(dir(Lipinski))
    print(Lipinski.NumHDonors(Chem.MolFromSmiles('OCCc1c(C)[n+](cs1)Cc2cnc(C)nc2N'))) # vitamin B1
    print(Lipinski.NumHAcceptors(Chem.MolFromSmiles('OCCc1c(C)[n+](cs1)Cc2cnc(C)nc2N'))) # vitamin B1
    print(Lipinski.NumAromaticRings(Chem.MolFromSmiles('OCCc1c(C)[n+](cs1)Cc2cnc(C)nc2N'))) # vitamin B1
    print(Lipinski.rdMolDescriptors(Chem.MolFromSmiles('OCCc1c(C)[n+](cs1)Cc2cnc(C)nc2N'))) # vitamin B1
    print(Lipinski.RingCount(Chem.MolFromSmiles('OCCc1c(C)[n+](cs1)Cc2cnc(C)nc2N'))) # vitamin B1




#target = new_client.target
#target_query = target.search('aromatase')
#targets = pd.DataFrame.from_dict(target_query)
#print(targets.target_chembl_id[0])

#target = new_client.target
#target_query = target.search('cox')
#targets = pd.DataFrame.from_dict(target_query)
#print(targets)
#print(targets.target_chembl_id[0])




# https://github.com/dataprofessor/code/tree/master/python
from chembl_webresource_client.new_client import new_client
from padelpy import from_smiles         #https://github.com/ecrl/padelpy         A Python wrapper for PaDEL-Descriptor And Pubchem Fingerprint
activity = new_client.activity              # https://www.ebi.ac.uk/chembl/         # database 

selected_target = 'CHEMBL3927'   
selected_target = "CHEMBL1075025"
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")

df = pd.DataFrame.from_dict(res)

#print(df.canonical_smiles[0])       # use https://www.novoprolabs.com/tools/smiles2pdb to see the compound
#print(df.standard_value[0])


#print(len(df))
desc_fp = from_smiles(df.canonical_smiles[0] , fingerprints=True, descriptors=False)  # use https://github.com/raghavagps/Pfeature to generate features for peptides  ==> https://github.com/dataprofessor/peptide-ml/blob/main/Antimicrobial_Peptide_QSAR.ipynb
#print((desc_fp))     # 880 fingerprints PubchemFP0-880   # https://web.cse.ohio-state.edu/~zhang.10631/bak/drugreposition/list_fingerprints.pdf 



def remove_low_variance_columns(df, threshold=0.1):
    """
    Remove columns with low variance.
    """
    # Calculate the variance of each column
    variances = df.var(axis=0)
    # Remove columns with low variance
    df.drop(df.columns[variances < threshold], axis=1, inplace=True)
    return df
