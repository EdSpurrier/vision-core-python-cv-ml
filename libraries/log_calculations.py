import math


def CalculateDiameter(label_width, real_label_width, log_diameter):
    percentageToLabel = log_diameter / label_width
    realDiameter = percentageToLabel * real_label_width
    diameterInCM = realDiameter / 10
    return diameterInCM


def CalculateJAS(log_diameter):
    jasDiameter = 0

    if log_diameter > 16:
        jasDiameter = math.floor(log_diameter / 2.) * 2
    else:
        jasDiameter = math.floor(log_diameter)

    return jasDiameter


def CalculateCBM(invoice_length, jas_sed_log_diameter):

    cbm_cal = jas_sed_log_diameter * jas_sed_log_diameter
    cbm_divide = cbm_cal / 10000
    cbm_ouput = cbm_divide * invoice_length

    return round(cbm_ouput, 3)