class Recipe {
    private String name;
    private String[] ingredients;
    private int[] ingreSizes;

    public Recipe(String name, String[] ingredients, int[] ingreSizes) {
        this.name = name;
        this.ingredients = ingredients;
        this.ingreSizes = ingreSizes;
    }

    public String getName() { return name; }
    public String[] getIngredients() { return ingredients; }
    public int[] getIngreSizes() { return ingreSizes; }
}