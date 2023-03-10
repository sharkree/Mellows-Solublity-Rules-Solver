# Source: https://usaco.guide/general/io

# fyi that line wraps are neglected lol

group_1 = {"H", "Li", "Na", "K", "Rb", "Cs"}
group_2 = {"Be", "Mg", "Ca", "Sr", "Ba"}
select_group_2 = {"Ca", "Sr", "Ba"}
weak_polyatomics = {"NO3", "C2H3O2", "CH3COO", "ClO4"}
insoluble_metals = {"Ag", "Pb", "Hg"}
select_halogens = {"Cl", "Br", "I"}
insoluble_anions = {"CO3", "CrO4", "PO4", "S", "O", "OH"}

# these are from an additional polyatomic ions reference sheet i found on schoology from last semester.
minus_one_charge = {"H", "F", "Cl", "Br", "I", "CH3COO", "C2H3O2", "N3", "BrO3", "ClO3", "ClO2", "CN", "H2PO4", "HCO3", "HSO4", "HSO3", "OH", "ClO", "NO3", "NO2", "ClO4", "MnO4", "SCN"}
minus_two_or_three_charge = {"CO3", "CrO4", "Cr2O7", "HPO4", "MnO4", "C2O4", "O2", "SiO3", "SO4", "SO3", "S2O3", "AsO4", "PO4", "PO3"}

# cation = input("Cation: \n")
# anion = input("Anion: \n")

cation = input("Input cation(no charges nor coefficients please): \n").strip()
anion = input("Input anion(no charges nor coefficients please): \n").strip()

# rule 1
if cation == "NH4" or cation in group_1:
    print("soluble")

# rule 2
elif anion in weak_polyatomics:
    print("soluble")

# rule 3
elif cation in insoluble_metals:
    print("insoluble")

# rule 4
elif anion in select_halogens:
    print("soluble")

# rule 5
elif anion in insoluble_anions:
    if cation in group_2:
        if anion in {"CrO4", "OH"}:
            if cation == "Ba" and anion == "CrO4":
                print("insoluble")
            elif cation == "Mg" and anion == "OH":
                print("insoluble")
            else:
                print("soluble")
        else:
            print("insoluble")
    else:
        print("insoluble")

# rule 6
elif anion == "SO4":
    if cation in {"Ba", "Ca", "Sr"}:
        print("insoluble")
    else:
        print("soluble")

# the two clauses at the bottom of the half sheet
else:
    print("Disclaimer: This part is because of the two clauses at the bottom of the half sheet. You will likely not have to use this but if it does happen, Mellows didn't explicitly teach this so it might be wrong. You have been warned.")
    if anion in minus_one_charge:
        print("soluble")
    elif anion in minus_two_or_three_charge:
        print("insoluble")
    else:
        print("please try something that works next time :)))")

print("And if this is wrong, please report any issues using github issues. Thanks for using!")
