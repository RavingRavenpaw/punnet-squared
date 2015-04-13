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
    print(genotypesList)
