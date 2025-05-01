import json

def save_all_borrowers(all_borrowers):
    with open("all_borrowers.json","w") as fp:
        json.dump(all_borrowers,fp, indent=4)