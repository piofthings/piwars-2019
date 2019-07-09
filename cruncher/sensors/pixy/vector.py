class Vector (Structure):
    _fields_ = [
        ("x0", c_uint),
        ("y0", c_uint),
        ("x1", c_uint),
        ("y1", c_uint),
        ("index", c_uint),
        ("flags", c_uint)]
