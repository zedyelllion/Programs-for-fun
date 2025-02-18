class Inventory {
    private String[] ingredients;
    private int[] ingreSizes;
    private int beverageStock;
    private int numIngredients;// count the total number of ingredients
    private int reOrderThreshold;
    public Inventory(String[] ingredients,int[] ingreSizes, int reOrderThreshold) {
        this.ingredients = ingredients;
        this.ingreSizes = ingreSizes;
        this.beverageStock = 0;
        this.numIngredients = ingredients.length;
        this.reOrderThreshold = reOrderThreshold;
    }

    public boolean checkIngredient(Recipe recipe, int batchSize) {
    	boolean check = true;// check is true when all items are sufficient to brew the required amount of recipe
    	for(int i=0;i<recipe.getIngredients().length;i++) {
    		for(int j=0;j<ingredients.length;j++) {
    			if(ingredients[j].equals(recipe.getIngredients()[i])) {
    				if(ingreSizes[j] < batchSize * recipe.getIngreSizes()[i]) {
    					check = false;
    					int shortage = batchSize * recipe.getIngreSizes()[i] - ingreSizes[j];
    					System.out.println("We need to buyin "+ shortage + " amount of "+ ingredients[j]);
    				}
    			}
    		}
    	}
    	return check;
    }
    
    public void deductIngredient(Recipe recipe, int batchSize) {
    	for(int i=0;i<recipe.getIngredients().length;i++) {
    		for(int j=0;j<ingredients.length;j++) {
    			if(ingredients[j].equals(recipe.getIngredients()[i])) {
    				ingreSizes[j] -= batchSize * recipe.getIngreSizes()[i];
    			}
    		}
    	}
    }
    
    public void addIngredient(String ingredient, int amount) {
    	boolean alreadyIn = false;
    	for(int i=0;i<ingredients.length;i++) {
    		if(ingredient.equals(ingredients[i])) {
    			alreadyIn = true;
    			ingreSizes[i] += amount;
    			break;
    		}
    	}
    	if(!alreadyIn) {
    		String[] newIngredients = new String[ingredients.length + 1];
    		int[] newIngreSizes = new int[ingreSizes.length + 1];
            // Copy old ingredients into the new array
            System.arraycopy(ingredients, 0, newIngredients, 0, ingredients.length);
            System.arraycopy(ingreSizes, 0, newIngreSizes, 0, ingreSizes.length);
            // Add the new ingredient to the last position
            newIngredients[ingredients.length] = ingredient;
            newIngreSizes[ingreSizes.length] = amount;
            // Update the Inventory attribute with the new array
            this.ingredients = newIngredients;
            this.ingreSizes = newIngreSizes;
            this.numIngredients += 1;
    	}
    	
    }
    
    public String[] getIngredients() {
    	return ingredients;
    }
    
    public int[] getIngreSizes() {
    	return ingreSizes;
    }
    public void addBeverageStock(int amount) { beverageStock += amount; }
    public void removeBeverageStock(int amount) { beverageStock -= amount; }
    public int getBeverageStock() { return beverageStock; }
}