package Patterns.Proxy_Pattern;

public class Printer implements IPrinter{

    private IPrinter printer;

    public Printer(){
        this.printer = new CLPrinter();
    }

    @Override
    public void print(String doc) {
        this.printer.print(doc);
    }

    public void switchPrinter(IPrinter printer){
        this.printer = printer;
    }
    
}