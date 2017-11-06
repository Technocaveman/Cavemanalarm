# control_any_auto.py  29/05/2016  D.J.Whale
#
# Demonstrates the variable auto-create.
#
# Variables are auto created into a given context, entirely from the registry.
# You should seed the registry first with setup_tool.py and give the devices
# the correct names, before this will work.

import time
import energenie

APP_DELAY = 1

def auto_loop():

    # Use the auto-generated variables 'fan' and 'tv'.
    # These can be any device that has a switch.
    # They must be defined with these names in the registry for this code to work.
    
    fan.turn_on()
    time.sleep(APP_DELAY)

def run_func():
    energenie.init()
    # Load all devices into variables auto created in the global scope
    # You can pass any context here, such as a class to contain your devices
    import sys
    me_global = sys.modules[__name__]
    energenie.registry.load_into(me_global)

    try:
        count = 0
        while count < 2:
            auto_loop()
            count = count + 1

    finally:
        energenie.finished()


if __name__ == "__main__":
    run_func()

# END
