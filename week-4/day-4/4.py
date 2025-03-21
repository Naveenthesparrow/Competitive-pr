https://leetcode.com/problems/boats-to-save-people/description/ 

Question Name: Boats Save People

lass Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the list of people in ascending order of weight
        people.sort()
        
        # Initialize pointers for the lightest and heaviest person
        left = 0
        right = len(people) - 1

        # Initialize the number of boats needed
        boats = 0

        # Loop through the list of people until 
        # all people have been rescued
        while left <= right:
            # Check if the lightest and heaviest person on 
            # the same boat can fit
            if people[left] + people[right] <= limit:
                # If they can, move on to the next lightest person
                left += 1
            # Move on to the next heaviest person
            right -= 1

            # Add a boat for the current group of people
            boats += 1
        # Return the total number of boats needed
        return boats