package Patterns.Proxy_Pattern;

public class SWPrinter implements IPrinter{

    @Override
    public void print(String doc) {
        System.out.println("SW printing: " + doc);
    }
    
}
