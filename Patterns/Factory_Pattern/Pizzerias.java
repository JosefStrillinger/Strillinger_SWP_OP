package Patterns.Factory_Pattern;

class HamburgPizzeria extends Pizzeria{

    @Override
    public void bakeSpezial() {
        System.out.println("No");
    }

}

class RostockPizzeria extends Pizzeria{

    @Override
    public void bakeSpezial() {
        System.out.println("Rostock Spezial wird zubereitet usw.");
    }

}

class BerlinPizzeria extends Pizzeria{

    @Override
    public void bakeSpezial() {
        System.out.println("Berlin Spezial wird zubereitet usw.");
    }

}
