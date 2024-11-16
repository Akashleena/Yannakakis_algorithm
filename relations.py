relations = {
    "R1": {"A":[1,2,3], "B": ["x", "y", "z"]},
    "R2": {"B": ["x", "z"], "C": [10,30]}
}

join_tree = [("R1", "R2")]

#Function to print relations
def print_relation(name, relation):
    print(f"Relation {name}:")
    for key in relation:
        print(f" {key}: {relation[key]}")
    print()

#Function to print join tree
def print_join_tree(tree):
    print("Join Tree:")
    for parent, child in tree:
        print(f" Parent: {parent}, Child: {child}")
    print()

#Main function
def main():
    for name, relation in relations.items():
        print_relation(name, relation)
    
    #Print the join tree
    print_join_tree(join_tree)

if __name__=='__main__':
    main()
