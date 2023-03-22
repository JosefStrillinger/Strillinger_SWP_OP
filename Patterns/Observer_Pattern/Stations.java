package Patterns.Observer_Pattern;

import java.util.ArrayList;
import java.util.List;

abstract class Stations {

    protected List<Display> displayList = new ArrayList<Display>();

    public void addDisplay(Display display) {
        displayList.add(display);
    }

    public void removeDisplay(Display display) {
        displayList.remove(display);
    }

    // Push
    protected void sendData(Weather weather){
        for (Display display : displayList){
            display.getWeather(weather);
        }
    }

    // Pull
    protected void notifySubscribers(){
        for (Display display : displayList){
            break;
        }
    }
}
