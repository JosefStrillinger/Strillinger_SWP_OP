package Patterns.Observer_Pattern;

public class Weather {
    private String weatherData;

    public Weather(String data){
        this.weatherData = data;
    }

    public String getWeatherData(){
        return this.weatherData;
    }
}
