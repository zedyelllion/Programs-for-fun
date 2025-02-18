class ProductionSystem {
    private Inventory inventory;
    private int numDirtyContainers;
    public ProductionSystem(Inventory inventory) {
        this.inventory = inventory;
        this.numDirtyContainers = 0;
    }

   

    public void bottleBeverage(int amount) {
        if (inventory.getBeverageStock() >= amount) {
            inventory.removeBeverageStock(amount);
            System.out.println(amount + " bottles have been filled and stored.");
            numDirtyContainers += amount;
        } 
        else {
            System.out.println("Not enough beverage stock for bottling.");
        }
    }
    
    public int getDirty() {
    	return numDirtyContainers;
    }
    
    public void cleanDirty() {
    	numDirtyContainers = 0;
    }
}