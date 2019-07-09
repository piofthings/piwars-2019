class Blocks (Structure):
    _fields_ = [("signature", c_uint),
                ("x", c_uint),
                ("y", c_uint),
                ("width", c_uint),
                ("height", c_uint),
                ("angle", c_uint),
                ("index", c_uint),
                ("age", c_uint)]
