# polybar-meteo

A simple script to retrive data from [meteo.pileus.si](meteo.pileus.si) and display it as a polybar module

## Example configuration:
```txt
[module/meteo]  
type = custom/script  
exec = "/path/to/polybar-meteo.py"  
interval = 60
```
