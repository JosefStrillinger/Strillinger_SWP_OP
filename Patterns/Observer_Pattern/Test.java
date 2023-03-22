package Patterns.Observer_Pattern;

public class Test {
    public static void main(String[] args){
        Station s = new Station();
        Display d1 = new Display("Display1");
        Display d2 = new Display("Display2");
        s.addDisplay(d1);
        s.addDisplay(d2);
        Weather Sun = new Weather("Sun - 25 °C");
        Weather Rain = new Weather("Rain | 14 °C");
        s.setWeatherPush(Sun);
        s.removeDisplay(d1);
        s.setWeatherPush(Rain);
        System.out.println("-----------------------");
        s.setWeatherPull(Sun);
        s.addDisplay(d1);
        s.setWeatherPush(Rain);


    }
}
