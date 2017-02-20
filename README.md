# RocketLogs
rocket flight log tracker with rest api

## Running
Docker image available at https://hub.docker.com as [colinzeidler/rocketlogs](https://hub.docker.com/r/colinzeidler/rocketlogs/)
```docker run -p 8000:8000 colinzeidler/rocketlogs``` you can add the ```-d``` flag if you want it to run in the background.
But you should really make sure to switch over from development mode to a real deployment setup (i.e. no debug mode, run with a wsgi, and clear out the database)... 

## TODOs
 * Authenticate Users
  * Users can only associate rockets with themselves and logs with thier rockets, and only modify thier rockets / logs
 * support events.
  * an event can have users associate with them, and add flights that occured during the event.
 * images of rockets
  * who doesn't like pretty pictures
