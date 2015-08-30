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
    cat1Genotype = raw_input("Genotype of Cat 1: ")
    print("")


    #2nd cat
    print("What is the genotype of the 2nd cat?")
    cat2Genotype = raw_input("Genotype of Cat 2: ")
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
    
    #Print a table showing the results of the cross
    #
    #It's really basic atm, but it's padded and the data lines up
    #correctly, so it doesn't matter. I'll make it look pretty
    #later.
    print "    %s  %s  " % (cat1Allele1, cat1Allele2)
    print "%s  %s  %s  " % (cat2Allele1, offspring1, offspring2)
    print "%s  %s  %s  " % (cat2Allele2, offspring3, offspring4)
    
#Run the program once the file is executed
cross()
