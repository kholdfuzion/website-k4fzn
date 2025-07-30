Title: Building a Hammo Can
Date: 07.30.2025 11:51
Category: Articles
Tags: ham radio, hammo can, portable, aprs

Recently, the STEM Amateur Radio Club lost a pico balloon (N4TVV-2), so I decided to build a "Hammo Can" to help in the hunt. It's a 50-caliber ammo can containing a 15Ah LiFePO4 battery with BMS, a Raspberry Pi Zero W 2, a 2.8" screen, an AIOC, a Baofeng AR-5RM, GPS dongle, a voltage monitor, USB ports, switches, and miscellaneous hookup components.

![Hammo Can Overview]({static}/images/hammo-can-overview.jpg)
*The completed Hammo Can setup*

## Components and Setup

The Pi runs DigiPi software, as it already does everything I need for APRS logging. Just complete the first-time setup and you're good to go. At home, it connects to a convenient antenna, and on the road, I have a port to connect whatever is easiest in the field.

![Internal Components]({static}/images/hammo-can-internal.jpg)
*Internal layout showing the battery, Pi, and radio components*

## Power Management

I also have a port for solar hookup with my accompanying panel. Since the radio operates mostly in listening mode, it's more than enough to fully charge the battery on most days.

![Solar Setup]({static}/images/hammo-can-solar.jpg)
*Solar panel for field operations*

## Field Testing

Field testing is still to come. It does work great around the house during initial testing.


## Future Plans

I plan to replace the AIOC and AR-5RM with an SA828S-V and a CM108 sound card. I would like to repurpose my radio and AIOC for other projects. I have several CM108 sound cards that I've modified and tested with an SA818, which is only a 1W module compared to the 2W SA828.

![Future Components]({static}/images/hammo-can-future-parts.jpg)
*SA818S-V and CM108 sound card test setup*