def make_chai():
    if not kettle_has_water():
        fill_kettle()
    plugin_in__kettle()
    boil_kettle()
    if not is_cup_clean():
        wash_cup()
    add_to_cup("tea leaves")
    add_to_cup("sugar")
    pour("boiled water")
    stie("cup")
    serve("chai")

make_chai()