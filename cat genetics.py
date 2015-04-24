import random

def cross():
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
    print("PLEASE PLACE DOMINANT ALLELES BEFORE RECESSIVE ALLELES")
    print("AND USE CORRECT CAPITALISATION")
    cat1Genotype = raw_input("Genotype of Cat 1: ")


    #2nd cat
    print("What is the genotype of the 2nd cat?")
    print("PLEASE PLACE DOMINANT ALLELES BEFORE RECESSIVE ALLELES")
    print("AND USE CORRECT CAPITALISATION")
    cat2Genotype = raw_input("Genotype of Cat 2: ")
    #Let's do some math!
    
    genotypesList = [cat1Genotype, cat2Genotype]
    #Get alleles
    
    #Cat 1
    cat1Allele1 = (cat1Genotype[:1])
    print(cat1Allele1)
    cat1Allele2 = (cat1Genotype[1:2])
    print(cat1Allele2)
    
    #Cat 2
    cat2Allele1 = (cat2Genotype[:1])
    print(cat2Allele1)
    cat2Allele2 = (cat2Genotype[1:2])
    print(cat2Allele2)
    
    
    '''
    #Dihybrid cross stuff
    #I put a bit of stuff in here, but idk if I'll be doing
    #anything that requires a dihybrid cross yet, so I'll
    #leave this commented out for now
    
    #Get gametes
    cat1Gamete1 = (cat1Allele1 + cat1Allele2)
    cat1Gamete2
    cat1Gamete3
    cat1Gamete4
    '''
    
    #Now to combine the alleles
    
    offspring = [(cat1Allele1 + cat2Allele1), (cat1Allele1 + cat2Allele2), (cat1Allele2 + cat1Allele1), (cat1Allele2 + cat2Allele2)]
    print(offspring)
