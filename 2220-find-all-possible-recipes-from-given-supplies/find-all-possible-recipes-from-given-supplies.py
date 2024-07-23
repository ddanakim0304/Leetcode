from collections import deque, defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Convert initial supplies list to a set for O(1) lookups
        supplies_set = set(supplies)
        
        # Prepare the graph and in-degree count
        recipe_graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        # Initialize the graph and in-degree
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                recipe_graph[ingredient].append(recipe)
                in_degree[recipe] += 1
        
        # Queue for processing recipes whose ingredients are all available
        queue = deque()
        
        # Add initial supplies to the queue
        for supply in supplies:
            queue.append(supply)
        
        # List to store the result recipes
        result = []
        
        # Process the queue
        while queue:
            ingredient = queue.popleft()
            
            # Check all recipes that can be made using this ingredient
            for recipe in recipe_graph[ingredient]:
                in_degree[recipe] -= 1
                # If in-degree of a recipe is 0, it means we can create it
                if in_degree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)
                    supplies_set.add(recipe)
        
        return result