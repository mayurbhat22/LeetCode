#Link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        recipes_set = {r for r in recipes}
        adj_list = defaultdict(list)
        indegree = {}

        for i in range(n):
            for ing in ingredients[i]:
                adj_list[ing].append(recipes[i])
                indegree[recipes[i]] = indegree.get(recipes[i], 0) + 1
        
        q = deque()
        answer = []
        for s in supplies:
            q.append(s)
        
        while q:
            s = q.popleft()

            if s in recipes_set:
                answer.append(s)

            for r in adj_list[s]:
                indegree[r] = indegree.get(r, 0) - 1
                if indegree[r] == 0:
                    q.append(r)
        return answer
             


"""
Topological Sort problem.
In Topo Sort, order is important.
So, create a adj_list starting from ingredients, since Ingredients make up a recipe.
Indegree of recipes will be how many ingredients it requires.
If a recipe requires another recipe as a prerequsite, then even that will be a indegree for that recipe.

Now, add all the supplies into the queue, since we can only make a recipe with some initial supplies.
So, for each supply, check what recipe it is making and decrease the indegre[recipe] -= 1. Meaning, one of the supply was present to make the recipe. If indegree is 0, then add it to the queue.
If after popping an element from the queue, which is the supply here, is a recipe, add it to the answer.
If we do not have a initial supply for any of the recipe, that recipe will not be created since the indegree will never becomes 0.
And, if some other recie is dependent on this recpe as the base, even that will not be prepared or will not be in the answer.
"""