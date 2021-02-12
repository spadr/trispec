# trispec.py
Calibration for SparkFun Triad Spectroscopy Sensor Development Board by temperature 

# Hardware
https://www.sparkfun.com/products/15050

# Usage
import trispec
data = [ 410nm_value,<br>
         435nm_value,<br>
         460nm_value,<br>
         485nm_value,<br>
         510nm_value,<br>
         535nm_value,<br>
         560nm_value,<br>
         585nm_value,<br>
         610nm_value,<br>
         645nm_value,<br>
         680nm_value,<br>
         705nm_value,<br>
         730nm_value,<br>
         760nm_value,<br>
         810nm_value,<br>
         860nm_value,<br>
         900nm_value,<br>
         940nm_value,<br>
         Measuring temperature]<br>
calibration_values = trispec.calibration(data) #return Calibrated values(20℃, ISO 1)
