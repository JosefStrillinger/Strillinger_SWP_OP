package Patterns.Observer_Pattern;

import java.util.ArrayList;
import java.util.List;

public class Station extends Stations{
    
    private Weather weather;

    @Override
    protected void notifySubscribers(){
        for (Display display : displayList){
            display.sendNotification(this);
        }
    }

    // Push
    public void setWeatherPush(Weather weather){
        this.weather = weather;
        sendData(weather);
    }

    // Pull
    public void setWeatherPull(Weather weather){
        this.weather = weather;
        notifySubscribers();
    }

    // Push
    public Weather getWeatherPush(){
        return this.weather;
    }

    // Pull
    public Weather getWeatherPull(){
        return this.weather;
    }
}
