import java.util.Scanner;
public class Main {
	public static String[] addString(String[] array, String newElement) {
	    String[] newArray = new String[array.length + 1];  // Create a new array with 1 extra slot
	    System.arraycopy(array, 0, newArray, 0, array.length);  // Copy old elements
	    newArray[array.length] = newElement;  // Add the new element
	    return newArray;
	}
	
	public static boolean contains(String[] array, String target) {
        for (String element : array) {
            if (element.equals(target)) {
                return true; // Found
            }
        }
        return false; // Not found
    }
	
	public static int[] addInt(int[] array, int newElement) {
	    int[] newArray = new int[array.length + 1];  // Create a new array with 1 extra slot
	    System.arraycopy(array, 0, newArray, 0, array.length);  // Copy old elements
	    newArray[array.length] = newElement;  // Add the new element
	    return newArray;
	}
	
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] allIngredients = {};
        int[] allIngreSizes = {};
        int reOrderThreshold = 100;
        Inventory inventory = new Inventory(allIngredients,allIngreSizes,reOrderThreshold);
        ProductionSystem production = new ProductionSystem(inventory);
        RecipeLibrary recipeLibrary = new RecipeLibrary(100);
        while(true) {
        System.out.println("Hi, you are in charge of a Brewery System. Press 1 to add a recipe, press 2 to check and clean the containers, "
        		+ "press 3 to to create a batch of beverages of your choice, press 4 to check or add for stockings of all ingredients,"
        		+ "press 5 to bottle beverage into containers, press 6 to quit.");
        int option = scanner.nextInt();
        //production.makeBatch(beerRecipe, batchSize);
        if(option == 1) {
        	System.out.println("Please enter the new recipe in the format 'RecipeName ingredient1 ingredient1Size ingredient2 ingredient2Size ...'"
        			+ "type R to return to the homepage.");
        	// I assume that recipe add up to 1 batchsize of beverage, to avoid for division to float problem. 
        	String newRecipeName = scanner.next();
        	String[] recipeIngredients = {};
        	int[] recipeIngreSizes = {};
        	while (true) {
                String input = scanner.next();
                if(input.equals("R")) {break;}
                String ingredient = input;
                int size = scanner.nextInt();
                recipeIngredients = addString(recipeIngredients,ingredient);
                recipeIngreSizes = addInt(recipeIngreSizes,size);
                if(!contains(inventory.getIngredients(),ingredient)) {
                	System.out.println("The inventory currently does not have any "+ingredient+" do you want to add it and buyin? Yes/No");
                	String yesNo = scanner.next();
                	if(yesNo.equals("No")) {break;}
                	System.out.println("Type in the amount you want to buyin.");
                	int buyinAmount = scanner.nextInt();
                	inventory.addIngredient(ingredient,buyinAmount);
                }
                
                //System.out.println("Ingredient: " + ingredient + ", Quantity: " + quantity);
            }
        	Recipe newRecipe = new Recipe(newRecipeName,recipeIngredients,recipeIngreSizes);
        	recipeLibrary.addRecipe(newRecipe);
        }
        else if(option == 2) {
        	System.out.println("There are "+ production.getDirty()+"dirty containers, the system will begin the cleaning process now.");
        	production.cleanDirty();
        }
        
        else if(option == 3) {
        	Recipe[] recipes = recipeLibrary.getRecipes();
        	System.out.println("Available Recipes:");
            for (int i = 0; i < recipeLibrary.getRecipeCount(); i++) {
                System.out.println((i + 1) + ". " + recipes[i].getName()); // Numbered List
            }
            System.out.println("Please enter the name of the beverage followed by the number of that beverage you wish to brew:");
            String userChoice = scanner.next();
            int batchSize = scanner.nextInt();
            Recipe theRecipe = null;
            int index = -1;
            for(int i = 0; i < recipes.length;i++) {
            	if(recipes[i].getName().equals(userChoice)) {
            		theRecipe = recipes[i];
            		index = i;
            		break;
            	}
            }
            
            if(index == -1) {
            	System.out.println("Your choice is not in the recipe list, either add to it or select a new one.");
            }
            else {
            	if(inventory.checkIngredient(theRecipe,batchSize)) {
            		inventory.deductIngredient(theRecipe,batchSize);
            		System.out.println("The system has successfully brewed "+ batchSize + "amount of " + userChoice +" for you.");
            		inventory.addBeverageStock(batchSize);
            	}
            	else {
            		System.out.println("There's not enough stockings in the inventory, please buyin first before brewing.");
            	}
            }
        }
        else if(option == 4) {
        	for(int i=0;i<inventory.getIngredients().length;i++) {
        		System.out.println("There is " + inventory.getIngreSizes()[i] + "of" + inventory.getIngredients()[i] + "left.");
        		if(inventory.getIngreSizes()[i] < 100) {
        			System.out.println("The stock of "+ inventory.getIngredients()[i] + "has already drop below the threshold,please buyin more.");
        		}
        	}
        	System.out.println("Do you want to buyin more? Yes/No");
        	String buyin = scanner.next();
        	if(buyin.equals("Yes")) {
        		System.out.println("Type the name followed by the amount of the ingredient you want to buyin, type R to return to the main menu.");
        		while(true) {
        			String input = scanner.next();
        			if(input.equals("R")) {break;}
        			int buyinSize = scanner.nextInt();
        			inventory.addIngredient(input,buyinSize);
        		}
        		System.out.println("Buyin Successful!");
        	}
        }
        else if(option == 5) {
        	System.out.println("The system currently stored " + inventory.getBeverageStock() + " number of beverages, "
        			+ "please type in the number of beverages you wished to bottled.");
        	int bottledUp = scanner.nextInt();
        	production.bottleBeverage(bottledUp);
        }
        else if(option == 6) {
        	break;
        }
        else {
        	System.out.println("Invalid input.");
        }
        }
        scanner.close();
    }
}