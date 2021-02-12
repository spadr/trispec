# trispec.py
Calibration for SparkFun Triad Spectroscopy Sensor Development Board by temperature 

## Hardware
https://www.sparkfun.com/products/15050

## Usage
```
import trispec

data = [ 410nm_value,
         435nm_value,
         460nm_value,
         485nm_value,
         510nm_value,
         535nm_value,
         560nm_value,
         585nm_value,
         610nm_value,
         645nm_value,
         680nm_value,
         705nm_value,
         730nm_value,
         760nm_value,
         810nm_value,
         860nm_value,
         900nm_value,
         940nm_value,
         Measuring temperature(Celsius)]#All values are float
         
calibration_values = trispec.calibration(data) #return Standard values(293.15K, ISO 1)
```
