![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg)

# TrainLED2 - A dual RGB-LED driver for TinyTapeout2

A dual RGB-LED driver using the WS2812 protocol

A fully digital implementation of an RGB LED driver that accepts the WS2812 for data input. The design is fully clocked, so the timing parameters of the protocol depend on the clock rate. A pulse between 1 and 5 clock cycles on the input will be interpreted as a zero, longer pulses as a one. Each driver accepts 3x8=24 bit of input data to set the brightness of LED1,LED2 and LED3 (R;G;B). After 24 bit have been received, additional input bits are re-timed and forwarded to the data output.

After the data input was idle for 96 clock cycles, the input data is latched into the PWM engine and the data input is ready for the next data frame.

The PWM engine uses a special dithering scheme to allow flicker free LED dimming even for relatively low clock rates.  

Source and testbench can be found in the /sdc folder. Execute the shell script 'run.sh' to invoke the testbench.



# Original TinyTapeout2 readme

TinyTapeout is an educational project that aims to make it easier and cheaper than ever to get your digital designs manufactured on a real chip!

Go to https://tinytapeout.com for instructions!

## How to change the Wokwi project

Edit the [info.yaml](info.yaml) and change the wokwi_id to match your project.

## How to enable the GitHub actions to build the ASIC files

Please see the instructions for:

* [Enabling GitHub Actions](https://tinytapeout.com/faq/#when-i-commit-my-change-the-gds-action-isnt-running)
* [Enabling GitHub Pages](https://tinytapeout.com/faq/#my-github-action-is-failing-on-the-pages-part)

## How does it work?

When you edit the info.yaml to choose a different ID, the [GitHub Action](.github/workflows/gds.yaml) will fetch the digital netlist of your design from Wokwi.

After that, the action uses the open source ASIC tool called [OpenLane](https://www.zerotoasiccourse.com/terminology/openlane/) to build the files needed to fabricate an ASIC.

## Resources

* [FAQ](https://tinytapeout.com/faq/)
* [Digital design lessons](https://tinytapeout.com/digital_design/)
* [Join the community](https://discord.gg/rPK2nSjxy8)

## What next?

* Share your GDS on Twitter, tag it [#tinytapeout](https://twitter.com/hashtag/tinytapeout?src=hashtag_click) and [link me](https://twitter.com/matthewvenn)!
