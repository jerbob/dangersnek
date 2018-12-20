# DangerSnek
Intercept Google Maps direction requests, and inject nearby crime hotspots.

This was my (winning) solution to the Dunhumby challenge for [Hack Manchester Junior 2018](https://www.hac100.com/event/hack-jr-2018/). The [brief](https://www.dunnhumby.com/about-us/events/hackmanchester2018) for this challenge was to use open data to make the consumer's experience "less than optimal", and my team decided to script an extension for the `mitmdump` command line https proxy.

The extension intercepts GET requests to the Google Maps API, for all URLs that match `https://www.google.com/maps/dir`. The destination is then extracted from the request parameters, the nearest vehicle crime is located using [open police data](https://data.police.uk/), a new detour is added to the request, and finally the request is altered by mitmproxy.

All code for this solution was written in under 8 hours, and won us the Dunhumby first place prize. 
