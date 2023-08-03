#
# This file is part of Cynthion
#

import os

from ..board import CynthionBoard

class CynthionMoondancer(CynthionBoard):
    """ Class representing Cynthion base-boards running the Moondancer firmware. """

    # This field refers to the USB device version number
    #
    # digit 1:   major
    # digit 2:   minor
    # digit 3&4: patch version
    HANDLED_BOARD_VERSIONS = [
        0x0004, # r0.4
        0x0005, # r0.5
        0x0006, # r0.6
        0x0007, # r0.7
        0x1000, # r1.0.0
        0x1100, # r1.1.0
        0x1101, # r1.1.1
    ]

    # Currently, all Cynthion Moondancer boards have an ID of 0x10.
    HANDLED_BOARD_IDS = [0x10]

    BOARD_NAME = "Cynthion in Moondancer mode"

    # The Cynthion has six LEDs.
    SUPPORTED_LEDS = 6

    # All of the GPIO mappings accessible from the Cynthion pmod headers.
    # TODO: add pmod gpio mappings for cynthion
    GPIO_MAPPINGS = {
    }

    def initialize_apis(self):
        """ Initialize a new Cynthion connection. """

        # Set up the core connection.
        super(CynthionMoondancer, self).initialize_apis()

        # Create our simple peripherals.
        self._populate_simple_interfaces()

        # Initialize the fixed peripherals that come on the board...

        # Populate the per-board GPIO.
        if self.supports_api("gpio"):
            self._populate_gpio()

        # Add objects for each of our LEDs.
        self._populate_leds(self.SUPPORTED_LEDS)
