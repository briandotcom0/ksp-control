Setup:
    requires ksp mods:
        krpc
    on the pi:
        sudo raspi-config
            enable i2c
        sudo apt-get install python-smbus i2c-tools
install:
    cd @project root
    virtualenv env
    pip install -r requirements.txt
    