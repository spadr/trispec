import math

def calibration(data, SRT = 20.):
    MT = data[-1]#Measuring temperature
    OS = data[0:-1]#Optical spectrum
    log_bool = [True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
    a = [393.77, 98.752, 7.2000, 4.3000, -3.700, -68.42, -1.36, -1.700, -7.080, -1.0, -0.2, 0.1, 0.2, -0.45, -11.292, -14.62, (-0.0343*OS[16]+2.0114), 2.9600]
    b = [6324.1, 2845.5, 4958.8, 2067.4, 3578.4, 4602.2, 1982., 2204.8, 7270.2, 1325, 1547, 409, 509, 373.3, 1577.80, 2767.0, 1008.400000000000000000, 420.28]
    values_in_SRT = [i * math.log(SRT) + j if k else i * SRT + j for i,j,k in zip(a , b, log_bool)]
    values_in_MT = [i * math.log(MT) + j if k else i * MT + j for i,j,k in zip(a , b, log_bool)]
    standard_values = [i * j / k for i,j,k in zip(OS, values_in_SRT, values_in_MT)]
    return standard_values
