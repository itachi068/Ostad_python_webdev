import json

def restore_all_borrowers(all_borrowers):
    with open("all_borrowers.json","r") as fp:
        all_borrowers = json.load(fp)
    return all_borrowers