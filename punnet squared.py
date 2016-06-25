import random
#I'll be using this to make more realistic crosses later.
#Read about it in the wiki. I start talking about stuff like percentages in crosses.

def cross():

    #1st parent
    print("What is the genotype of the 1st organism?")
    cat1Genotype = input("Genotype of P1: ")
    print("")


    #2nd parent
    print("What is the genotype of the 2nd organism?")
    cat2Genotype = input("Genotype of P2: ")
    print("")
    
    #Let's do some math!
    #Get alleles
    
    #Parent 1
    P1Allele1 = (cat1Genotype[:1])
    P1Allele2 = (cat1Genotype[1:2])
    
    #Parent 2
    P2Allele1 = (cat2Genotype[:1])
    P2Allele2 = (cat2Genotype[1:2])
    
    #Combine the alleles into individual offspinrg
    F1_1 = (P1Allele1 + P2Allele1)
    F1_2 =  (P1Allele2 + P2Allele1)
    F1_3 = (P1Allele1 + P2Allele2)
    F1_4 =  (P1Allele2 + P2Allele2)
    
    
    #If the first allele is lowercase and the second is uppercase, switch the
    #alleles around so that the uppercase allele is first.
    
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #F1_1
    if P1Allele1 in lowercase_letters and P2Allele1 in uppercase_letters:
            F1_1 = (P2Allele1 + P1Allele1)
            
    #F1_2
    if P1Allele2 in lowercase_letters and P2Allele1 in uppercase_letters:
            F1_2 = (P2Allele1 + P1Allele2)
            
    #F1_3
    if P1Allele1 in lowercase_letters and P2Allele2 in uppercase_letters:
            F1_3 = (P2Allele2 + P1Allele1)
            
    #F1_4
    if P1Allele2 in lowercase_letters and P2Allele2 in uppercase_letters:
            F1_4 = (P2Allele2 + P1Allele2)

    #Get the /unique/ genotypes
    numGenotypes = 1
    genotypes = []
    genotype1 = F1_1
    genotypes.append(genotype1)
    if F1_2 != F1_1:
        genotype2 = F1_2
        numGenotypes += 1
        genotypes.append(genotype2) 
    else:
        genotype2 = ""   

    if F1_3 != F1_2 and F1_3 != F1_1:
        genotype3 = F1_3
        numGenotypes += 1
        genotypes.append(genotype3)
    else:
        genotype3 = ""

    if F1_4 != F1_3 and F1_4 != F1_3 and F1_4 != F1_2 and F1_4 != F1_1:
        genotype4 = F1_4
        numGenotypes += 1
        genotypes.append(genotype4)
    else:
        genotype4 = ""

    genotype1 = genotypes[0]
    genotype2 = genotypes[1] if numGenotypes >= 2 else None
    genotype3 = genotypes[2] if numGenotypes >= 3 else None
    genotype4 = genotypes[3] if numGenotypes == 4 else None


    #Convert the list of genotypes to a string
    #and clean it up
    genotypesStr = str(genotypes)
    genotypesStr = genotypesStr.replace(",", "")
    genotypesStr = genotypesStr.replace("[", "")
    genotypesStr = genotypesStr.replace("]", "")
    genotypesStr = genotypesStr.replace("\'", "")

    #Make offspring list
    offspring = [F1_1, F1_2, F1_3, F1_4]
    

    #Calculate what percent of offpsring are what genotype
    genotype1Amt = 0
    genotype2Amt = 0
    genotype3Amt = 0
    genotype4Amt = 0

    genotype1Amt = offspring.count(genotype1)
    genotype2Amt = offspring.count(genotype2) if numGenotypes >= 2 else None
    genotype3Amt = offspring.count(genotype3) if numGenotypes >= 3 else None
    genotype4Amt = offspring.count(genotype4) if numGenotypes == 4 else None
    
    
    #Print a table showing the results of the cross
    #
    #It's really basic atm, but it's padded and the data lines up
    #correctly, so it doesn't matter. I'll make it look pretty
    #later.
    print("    %s  %s  " % (P1Allele1, P1Allele2))
    print("%s  %s  %s  " % (P2Allele1, F1_1, F1_2))
    print("%s  %s  %s  " % (P2Allele2, F1_3, F1_4))
    print("")
    print("Genotypes: %s" % genotypesStr)
    print(str(genotype1Amt/4*100) + "% " + genotype1)
    print(str(genotype2Amt/4*100) + "% " + genotype2) if numGenotypes >= 2 else None
    print(str(genotype3Amt/4*100) + "% " + genotype3) if numGenotypes >= 3 else None
    print(str(genotype4Amt/4*100) + "% " + genotype4) if numGenotypes == 4 else None


def strCleanUp(oldStr):
    global newStr
    nsewStr = str(oldStr)
    newStr = oldStr.replace(",", "")
    newStr = oldStr.replace("[", "")
    newStr = oldStr.replace("]", "")
    newStr = oldStr.replace("\'", "")
#Run the program once the file is executed
cross()
