package Patterns.Factory_Pattern;

public class PizzeriaFactory {
    public static void main(String[] args) {
        Pizzeria h = new HamburgPizzeria();
        Pizzeria b = new BerlinPizzeria();
        Pizzeria r = new RostockPizzeria();

        b.bakePizza(Pizza.Calzone);
        h.bakePizza(Pizza.Calzone);
        r.bakeSpezial();
        b.bakeSpezial();
        h.bakeSpezial();
    }
}