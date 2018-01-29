""" @Author: Ajibola Ebunoluwa Vincent """
#   @Course: COSC 5340
#   @Professor: Dr Arun Kulkarni
#   @Description: Program to demonstrate Virtual Number to Page Number translation


# Import modules from random and math
import random
import math

# declare variables
virtual_bits = 14
physical_bits = 13
pagesize = 1024

# array of frame numbers
framenum = []
# array of page numbers
pagenum = []
# array of virtual numbers
virnum = []
# array of word numbers
wordnum = []


# Function to generate random numbers from 0-16383
def rand_fun():
    var = random.randint(0, 16384)
    return var


# Function to to generate random virtual addresses and append to lists(pagenum, virnum and wordnum)
def compute():
    bit_pagesize = virtual_bits - int(math.log(pagesize, 2))
    for i in range(0, 99):
        # generate 100 random number
        page_no = rand_fun()
        # append each number to the virnum array
        virnum.append(page_no)
        print("The Virtual Address generated is", page_no)
        # boolean check the length of the binary representation of the generated virtual number
        if page_no.bit_length() < 14:
            # if the bit_length is less than 14, pad the binary representation with 0s up to 14
            gen = str(bin(page_no)[2:]).zfill(virtual_bits)
            page_no = gen[0:bit_pagesize]
            page_no = int(page_no, 2)
            word = gen[bit_pagesize:]
            print("Its Page Number is", page_no, "and word is ", word)
            pagenum.append(page_no)
            wordnum.append(word)
        else:
            # if the bit_length is equal to 14
            # slice the string from the 3rd character to the end
            gen = str(bin(page_no)[2:])
            page_no = gen[0:bit_pagesize]
            page_no = int(page_no, 2)
            word = gen[bit_pagesize:]
            print("Its Page Number is", page_no, "and word is ", word)
            pagenum.append(page_no)
            wordnum.append(word)


# Function to Load frames and populate page table
def paging():
    # clean_page is a list without any duplicates eliminates duplicates
    clean_page = [pagenum[i] for i in range(len(pagenum)) if i == pagenum.index(pagenum[i])]
    # Initialize the Frame from 0-7
    for i in range(0, 8):
        framenum.append(i)
    # create a page table from the list of "clean" list of page numbers and the frame number list
    page_table = dict((k, v) for k, v in zip(clean_page, framenum))
    # create a dictionary to map the virtual address generate and its word number
    virtual_word = dict((k, v) for k, v in zip(virnum, wordnum))
    # create a dictionary to map the virtual address generated and its page number
    virtual_page = dict((k, v) for k, v in zip(virnum, pagenum))
    print("Page Table:", page_table)
    # Return a tuple of values
    return page_table, virtual_word, virtual_page


# Function to lookup of page number from page table
def lookup(my_tuple):
    pt, vw, vp = my_tuple
    for k, v in vp.items():
        if v in pt.keys():
            # lookup page table and return page number
            ans = pt[v]
            # convert page number to binary and append to the word num from the virtual_word dictionary
            page_decimal = int(str(bin(ans) + vw[k]).zfill(physical_bits), 2)
            print("The physical address of the virtual address", k, " is ", page_decimal)
        else:
            print("The Page number of the virtual address", k, " is yet to be loaded, hence a Page Fault")


# Function to run program
def run():
    compute()
    lookup(paging())


if __name__ == "__main__":
    run()



