import os
from imagededup.methods import PHash

if __name__ == '__main__':
    phasher = PHash()
    duplicates_list = phasher.find_duplicates_to_remove('I://duplicatepic//001')
    for i in range(0,len(duplicates_list)-1):
        duplicates_list_remove = 'I://duplicatepic//001//'+duplicates_list[i]
        os.remove(duplicates_list_remove)
