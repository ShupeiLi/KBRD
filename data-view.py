import pickle as pkl
import os

datapath = ""

def report(number, name):
    file = pkl.load(open(
        os.path.join(datapath, 
                    f"./data/redial-{number}", 
                    f"{name}.pkl"), "rb"))
    print(f"{name}-{number}: {len(file)}")

for name in ["dbpedia", "entity2entityId", "id2entity", "movie_ids", "relation2relationId", "subkg"]:
    for number in [1, 2, 3]:
        report(number, name)