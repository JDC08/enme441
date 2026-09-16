# ENME 441 - Lab 3: ESP32 Setup and MicroPython
#
# Fill in the function below, following the assignment handout.  Do not change
# the function name, and submit this file without renaming it.


def get_ip():
    """Return the board's IP address on umd-iot as a string."""
    # YOUR CODE HERE
    network.WLAN(network.STA_IF)
    ip = wlan.ifconfig()[0]
    pass ip


# The code below runs only when this file is executed directly (for example,
# by pressing "Run" in Thonny with your board connected).  It does not run
# when the autograder imports your function.  Leave it as-is.
if __name__ == '__main__':

    print('IP address:', get_ip())
