import random

def cross():
    #L: Short hair
    #l: Long hair
    #l is dominant to L
    #
    #LL: Short haired cat
    #Ll: Short haired cat
    #ll: Long haired cat
    
    
    #1st cat
    print("Do you know the 1st cat's genotype or phenotype?")
    print("If phenotype is used, punnet squares with all possible")
    print("genotypes of the 1st cat will be created.")
    print("Using genotype will only use the genotype you specify.")
    print("")
    typeUsed = raw_input("Type P for Phenotype or G for Genotype: ")
    if typeUsed == ("G") or typeUsed == ("g"):
        print("You are using genotype.")
        print("What is the genotype of the 1st cat?")
        print("PLEASE PLACE DOMINANT ALLELES BEFORE RECESSIVE ALLELES")
        print("AND USE CORRECT CAPITALISATION")
        cat1Genotype = raw_input("Genotype of Cat 1: ")


    #2nd cat
    print("Do you know the 2nd cat's genotype or phenotype?")
    print("If phenotype is used, punnet squares with all possible")
    print("genotypes of the 2nd cat will be created.")
    print("Using genotype will only use the genotype you specify.")
    print("")
    typeUsed = raw_input("Type P for Phenotype or G for Genotype: ")
    if typeUsed == ("G") or typeUsed == ("g"):
        print("You are using genotype.")
        print("What is the genotype of the 2nd cat?")
        print("PLEASE PLACE DOMINANT ALLELES BEFORE RECESSIVE ALLELES")
        print("AND USE CORRECT CAPITALISATION")
        cat2Genotype = raw_input("Genotype of Cat 2: ")