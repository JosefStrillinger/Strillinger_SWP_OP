package Factory_Pattern;

public abstract class Pizzeria{
    public void bakePizza(Pizza p){
        System.out.println(p + " wird zu bereitet");
    }

    public abstract void bakeSpezial();
}
