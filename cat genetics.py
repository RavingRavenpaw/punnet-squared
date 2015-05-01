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
    
    offspring1 = (cat1Allele1 + cat2Allele1)
    offspring2 =  (cat1Allele1 + cat2Allele2)
    offspring3 = (cat1Allele2 + cat1Allele1)
    offspring4 =  (cat1Allele2 + cat2Allele2)

    #From tut, will erase later.
    #Using as reference to do stuff
    print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
    
    print "    %s  %s  " % (cat1Allele1, cat1Allele2)
    print "%s  %s  %s  " % (cat2Allele1, offspring1, offspring2)
    print "%s  %s  %s  " % (cat2Allele2, offspring3, offspring4)
    
    
'''
    #Make a table showing the cross
    
    #I was trying to make a table to show the cross (so basically a punnet swaure compsed
    #of characters
    #
    #I'll finish this later or change it into something different, but I'm dropping it for now
    print(" ",cat1Allele1," "," ",cat1Allele2," ",)
    print("---------")
    print("")

        



    #By Sven Marnach on Stack Overflow
    #http://stackoverflow.com/questions/8356501/python-format-tabular-output
    def print_table(table):
        col_width = [max(len(x) for x in col) for col in zip(*table)]
        for line in table:
            print "| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |"

table = (offspring)
print_table(table)
'''
