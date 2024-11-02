import pickle
file_names = ['/home/hice1/pbegwani3/scratch/maestro-cqt-final.pickle', '/home/hice1/pbegwani3/scratch/maestro-cqt-final-2.pickle', '/home/hice1/pbegwani3/scratch/maestro-cqt-final-3.pickle']


final_dict = {}
for fn in file_names:
    combined_data_3 = {}

    if 'final-2' in fn:
        offset = 517
    elif 'final-3' in fn:
        offset = 1048
    else:
        offset = 0

    with open(fn, 'rb') as f:
        unpickler = pickle.Unpickler(f)
        
        while True:
            try:
                item = unpickler.load()  # Load the next object in the file
                combined_data_3[list(item.keys())[0] + offset] = list(item.values())[0]
            except EOFError:
                break

    final_dict = {**final_dict, **combined_data_3}

print(len(final_dict))

chunk_size = 100  # Set a chunk size
output_file = '/home/hice1/pbegwani3/scratch/final_all_cqt.pickle'

with open(output_file, 'wb') as f:
    for i in range(0, len(final_dict), chunk_size):
        chunk = dict(list(final_dict.items())[i:i+chunk_size])
        pickle.dump(chunk, f)