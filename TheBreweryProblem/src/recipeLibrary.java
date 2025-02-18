class RecipeLibrary {
    private Recipe[] recipes;
    private int recipeCount;

    public RecipeLibrary(int capacity) {
        recipes = new Recipe[capacity];
        recipeCount = 0;
    }

    public void addRecipe(Recipe recipe) {
        if (recipeCount < recipes.length) {
            recipes[recipeCount++] = recipe;
            System.out.println("Recipe " + recipe.getName() + " added successfully.");
        }
        else {
            System.out.println("Recipe Library is full.");
        }
    }

    public Recipe getRecipe(String name) {
        for (Recipe recipe : recipes) {
            if (recipe != null && recipe.getName().equals(name)) {
                return recipe;
            }
        }
        return null;
    }
    
    public String[] getRecipeNames() {
    	String[] allkinds = new String[this.recipeCount];
    	for (int i = 0; i < allkinds.length; i++) {
    	    allkinds[i] = recipes[i].getName(); 
    	}
    	return allkinds;
    }
    
    public Recipe[] getRecipes() {
    	return recipes;
    }
    public int getRecipeCount() {
    	return recipeCount;
    }
}