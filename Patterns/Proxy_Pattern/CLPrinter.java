package Patterns.Proxy_Pattern;

public class CLPrinter implements IPrinter{

    @Override
    public void print(String doc) {
        System.out.println("COLOR printing: "+ doc);
    }
    
}
