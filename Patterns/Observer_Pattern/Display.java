package Patterns.Observer_Pattern;

public class Display implements Displays{

    private String displayName;

    public Display(String name){
        this.displayName = name;
    }

    // Push
    public void getWeather(Weather weather) {
        System.out.println(this.displayName + ": " + weather.getWeatherData());
    }

    public void sendNotification(Station station){
        System.out.println(this.displayName + ": " + station.getWeatherPull().getWeatherData());
    }
    
}
