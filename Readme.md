# Installation

The curl module of loboris' micropython has to be enabled inside of the micropython configuration in the `menuconfig` command along with mqtt and mdns.

To get startet a file called secrets.py has to be created.


    export IDF_PATH=$HOME/SOME-PATH/esp-idf
    export PATH=$HOME/Documents/SOME-PATH/xtensa-esp32-elf/bin:$PATH

    cd
    git clone --depth 1 https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo.git
    cd MicroPython_ESP32_psRAM_LoBo/MicroPython_BUILD
    ./BUILD.sh menuconfig
    ./BUILD.sh all  
    ./BUILD.sh flash
