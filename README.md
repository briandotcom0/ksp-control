Setup:
    requires ksp mods:
        krpc
install:
    cd @project root
    virtualenv env
    pip install -r requirements.txt
    