# https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/

def removeZeroes(list): # warmup 1
    while 0 in list:
        list.remove(0)

def descendingSort(list):  # warmup 2
    list.sort(reverse=True)

def lengthCheck(N, list):     # warmup 3
    # Given a number N and a sequence of answers, return true if N is greater than the number of answers (i.e. the length of the sequence), and false if N is less than or equal to the number of answers.
    if N < 0:
        raise ValueError("N cannot be negative.")
    return N > len(list)

def frontRemoval(N, list):
    if  N <= 0 or N > len(list):    # Assume 0 < N <= len(list)
        raise ValueError("N must satisfy: 0 < N <= len(list)")
    for i in range(N):
        list[i] -= 1
    return list

def HavelHakimi(list_of_answers):
    removeZeroes(list_of_answers)
    if len(list_of_answers) == 0:
        return True

    descendingSort(list_of_answers)
    N = list_of_answers.pop(0) # remove the first (and largest) answer
    if lengthCheck(N, list_of_answers):
        return False # return false if N is larger than amount of answers

    return HavelHakimi(frontRemoval(N, list_of_answers))

a = [16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]
print(HavelHakimi(a))













# ==========================================================
# ==========================================================
def HavelHakimi_debug(list_of_answers):
    print("=== NEW ITERATION ===")
    print("1. list at start: ", list_of_answers)

    #try:
    #    removeZeroes(list_of_answers)
    #except:
        #if not list_of_answers:
            #print("exception!")
            #return True
    removeZeroes(list_of_answers)
    print("2. removed zeroes: ", list_of_answers)

    if len(list_of_answers) == 0:
        return True

    descendingSort(list_of_answers)
    print("3. list sorted: ", list_of_answers)

    N = list_of_answers.pop(0) # remove the first (and largest) answer

    print("4. popped first index: ", list_of_answers)
    print("     N = ", N, ". len(list) = ", len(list_of_answers), ".")

    if lengthCheck(N, list_of_answers):
        return False # return false if N is larger than amount of answers

    print("5. N > len(list): ", lengthCheck(N, list_of_answers))
    print("6. front removal: ", frontRemoval(N, list_of_answers)) # replace frontRemoval if removing this print!
    print("list at end: ", list_of_answers)

    return HavelHakimi_debug(list_of_answers)
# ==========================================================
# ==========================================================
