import random
#I'll be using this to make more realistic crosses later.
#Read about it in the wiki. I start talking about stuff like percentages in crosses.

def cross():
    #BASIC INFO ON GENOTYPES, PHENOTYPES, AMD ALLELES
    #
    #L: Short hair
    #l: Long hair
    #L is dominant to l
    #Short hair is dominant to long hair
    #
    #LL: Short haired cat - Homo. Dom.
    #Ll: Short haired cat - Het. Dom.
    #ll: Long haired cat - Homo. Rec.
    
    
    #1st cat
    print("What is the genotype of the 1st cat?")
    cat1Genotype = input("Genotype of Cat 1: ")
    print("")


    #2nd cat
    print("What is the genotype of the 2nd cat?")
    cat2Genotype = input("Genotype of Cat 2: ")
    print("")
    
    #Let's do some math!
    #Get alleles
    
    #Cat 1
    cat1Allele1 = (cat1Genotype[:1])
    cat1Allele2 = (cat1Genotype[1:2])
    
    #Cat 2
    cat2Allele1 = (cat2Genotype[:1])
    cat2Allele2 = (cat2Genotype[1:2])
    
    #Combine the alleles into individual offspinrg
    offspring1 = (cat1Allele1 + cat2Allele1)
    offspring2 =  (cat1Allele2 + cat2Allele1)
    offspring3 = (cat1Allele1 + cat2Allele2)
    offspring4 =  (cat1Allele2 + cat2Allele2)
    
    
    #If the first allele is lowercase and the second is uppercase, switch the
    #alleles around so that the uppercase allele is first.
    
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #Kitten1
    if cat1Allele1 in lowercase_letters and cat2Allele1 in uppercase_letters:
            offspring1 = (cat2Allele1 + cat1Allele1)
            
    #Kitten2
    if cat1Allele2 in lowercase_letters and cat2Allele1 in uppercase_letters:
            offspring2 = (cat2Allele1 + cat1Allele2)
            
    #Kitten3
    if cat1Allele1 in lowercase_letters and cat2Allele2 in uppercase_letters:
            offspring3 = (cat2Allele2 + cat1Allele1)
            
    #Kitten4
    if cat1Allele2 in lowercase_letters and cat2Allele2 in uppercase_letters:
            offspring4 = (cat2Allele2 + cat1Allele2)

    #Get the /unique/ genotypes
    numGenotypes = 1
    genotypes = []
    genotype1 = offspring1
    genotypes.append(genotype1)
    if offspring2 != offspring1:
        genotype2 = offspring2
        numGenotypes += 1
        genotypes.append(genotype2) 
    else:
        genotype2 = ""   

    if offspring3 != offspring2 and offspring3 != offspring1:
        genotype3 = offspring3
        numGenotypes += 1
        genotypes.append(genotype3)
    else:
        genotype3 = ""

    if offspring4 != offspring3 and offspring4 != offspring3 and offspring4 != offspring2 and offspring4 != offspring1:
        genotype4 = offspring4
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
    offspring = [offspring1, offspring2, offspring3, offspring4]
    

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
    print("    %s  %s  " % (cat1Allele1, cat1Allele2))
    print("%s  %s  %s  " % (cat2Allele1, offspring1, offspring2))
    print("%s  %s  %s  " % (cat2Allele2, offspring3, offspring4))
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
