package Patterns.Proxy_Pattern;

public class ProxyPatternDemo {
    
    public static void main(String[] args){
        Printer printer = new Printer();

        printer.print("Test");

        printer.print("Ohhh color");

        printer.switchPrinter(new SWPrinter());

        printer.print("Oh no, color gone");
    }
}
