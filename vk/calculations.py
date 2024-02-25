def extremely_low(respiration, heart_rate, blushing_level, pupillary_dilation):
    """
    Determines if the vital signs indicate an extremely low state.

    :param respiration: The respiration rate.
    :type respiration: int
    :param heart_rate: The heart rate.
    :type heart_rate: int
    :param blushing_level: The level of blushing.
    :type blushing_level: int
    :param pupillary_dilation: The degree of pupillary dilation.
    :type pupillary_dilation: int
    :return: True if the vital signs indicate an extremely low state, False otherwise.
    :rtype: bool
    """
    if respiration < 12 or heart_rate < 60 or blushing_level < 1 or pupillary_dilation < 2:
        return True

def extremely_high(respiration, heart_rate, blushing_level, pupillary_dilation):
    """
    Determines if the vital signs indicate an extremely high state.

    :param respiration: The respiration rate.
    :type respiration: int
    :param heart_rate: The heart rate.
    :type heart_rate: int
    :param blushing_level: The level of blushing.
    :type blushing_level: int
    :param pupillary_dilation: The degree of pupillary dilation.
    :type pupillary_dilation: int
    :return: True if the vital signs indicate an extremely high state, False otherwise.
    :rtype: bool
    """
    if respiration > 20 or heart_rate > 120 or blushing_level > 4 or pupillary_dilation > 6:
        return True

def abnormal(respiration, heart_rate, blushing_level, pupillary_dilation):
    """
    Determines if the vital signs indicate an abnormal state.

    :param respiration: The respiration rate.
    :type respiration: int
    :param heart_rate: The heart rate.
    :type heart_rate: int
    :param blushing_level: The level of blushing.
    :type blushing_level: int
    :param pupillary_dilation: The degree of pupillary dilation.
    :type pupillary_dilation: int
    :return: True if the vital signs indicate an abnormal state, False otherwise.
    :rtype: bool
    """
    if heart_rate/respiration < 3 or heart_rate/respiration > 5:
        return True
    if heart_rate < 40 or heart_rate > 220:
        return True
    if pupillary_dilation < 2 or pupillary_dilation > 8:
        return True
    if (blushing_level <= 3 and heart_rate > 90) or (blushing_level > 3 and heart_rate < 70):
        return True

def calculate_decision(respiration, heart_rate, blushing_level, pupillary_dilation, score):
    """
    Calculates the decision based on vital signs and a score.

    :param respiration: The respiration rate.
    :type respiration: int
    :param heart_rate: The heart rate.
    :type heart_rate: int
    :param blushing_level: The level of blushing.
    :type blushing_level: int
    :param pupillary_dilation: The degree of pupillary dilation.
    :type pupillary_dilation: int
    :param score: The score for decision making.
    :type score: int
    :return: The decision value based on the vital signs and score.
    :rtype: int
    """
    if abnormal(respiration, heart_rate, blushing_level, pupillary_dilation):
        return 0
    if (extremely_high(respiration, heart_rate, blushing_level, pupillary_dilation) and score <= 2)\
        or (extremely_low(respiration, heart_rate, blushing_level, pupillary_dilation) and score > 2):
        return 50
    if (extremely_low(respiration, heart_rate, blushing_level, pupillary_dilation) and score < 2) \
        or (extremely_high(respiration, heart_rate, blushing_level, pupillary_dilation) and score > 2):
        return 100
    else:
        return 50


def final_decision(percent):
    """
    Prints the final decision based on the percentage value.

    :param percent: The percentage value.
    :type percent: int
    """
    if percent >= 50:
        print(f"\nPercent of human: {percent}%")
    elif percent < 50:
        print(f"\nPercent of replicant: {100-percent}%")
   