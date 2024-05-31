#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

#Question 1:

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: [2,3,4,2,7] target = 10, output = [1,4]

def twoSum(nums, target):
    for i in range(0, len(nums) - 1):       # iterate on the numbers minus the last one
        for j in range(i + 1, len(nums)):   # iterate on the remaining numbers
            if nums[i] + nums[j] == target: # found a match?
                return [i, j]               # if yes, return the indices list
    return []                               # otherwise return an empty list

#Time and space complexity:

#Question 2:
#Given some arrays with strings on them, find the most common longest prefix among them.
#Example: ["flower","flow","flight"] output = "fl"

def findMostCommonPrefix(arr):
    prefixes = {}                           # Empry dictionary to count the prefixes
    for word in arr:                        # Iterate on the words in the list
        length = len(word)                  # Get the length of the word
        for i in range(length, 1, -1):      # Iterate backwards from len of word to 1
            prefix = word[0:i]              # Get the prefix chars from 0 to i
            if prefix in prefixes.keys():   # If prefix already exist in keys
                prefixes[prefix] += 1       #     Increase the prefix count by 1    
            else:                           # If it doesn't exist in the keys
                prefixes[prefix] = 1        #     Add key with value of 1
    
    winner = max(prefixes.values())         # Find the maximum occurance count
    for key, value in prefixes.items():     # Iterate on Key, Values of the dict
        if value == winner:                 # If the count is maximum
            return key                      # Return the prefix
    

#Time and space complexity:

#Question 3:
#Given an array of integers, return the indices of three numbers that add up to 0.
#example: [1, 2, -2, -1, 3] output = [2, 3, 4]

def threeSum(nums):
    for i in range(0, len(nums) - 2):                 # iterate on the numbers minus the last two
        for j in range(i + 1, len(nums) - 1):         # iterate on the remaining from previous minus the last one
            for k in range(j + 1, len(nums)):         # iterate on the remaining from previous minus
                if nums[i] + nums[j] + nums[k] == 0:  # found a match?
                    return [i, j, k]                  # if yes, return the indices list
    return []  

#Time and space complexity:

#Question 4:
#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printList(head):
    while head:
        print(head.data)
        head = head.next

head   = Node(1)
middle = Node(2)
tail   = Node(3)

head.next   = middle
middle.next = tail
tail.next   = None

printList(head)
########################################################################################################
def reverseList(head):                      # Using Normal Loop
    nodes = []                              # Create an empty list
    node = head
    while node:                             # Gather all the nodes of the link list in a loop until next is None
        nodes.append(node)
        node = node.next
    
    nodes[0].next = None                    # make the head to become tail by poining to nowhere
    for i in range(1, len(nodes)):          # loop on the nodes starting from index 1
        nodes[i].next = nodes[i - 1]        # Make each node to point to the previous node
    
    return nodes[-1]                        # return the last item that is our new head
########################################################################################################
def reverseList(head):                      # Using Recursive
    if head == None or head.next == None:   # If head is None or Head is only 1 Node, nothing to reverse!
        return head                         # Return the one node or None
    newHead = reverseList(head.next)        # First go to the end of the stack to find the new head
    head.next.next = head                   # On the way back, make the next node to point to the current node
    head.next = None                        # ...and the current node to point to None.
    return newHead                          # Return the new Head back to the top of the stack
                                            # This one took so long to make it work :-(
########################################################################################################
newHead = reverseList(head)
printList(newHead)
#Time and space complexity:




