import os
from imagededup.methods import PHash
image_dir ='I://net hat//001'

if __name__ == '__main__':
    phasher = PHash()
    duplicates_list = phasher.find_duplicates_to_remove(image_dir)
    for i in range(0,len(duplicates_list)-1):
        duplicates_list_remove = image_dir + '//' + duplicates_list[i]
        os.remove(duplicates_list_remove)
