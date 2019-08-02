import random
import pyDes
import time
import base64


class Captcha:
    VALID_CHARS = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"

    PYDES = None

    def __init__(self, key):
        self.PYDES = pyDes.triple_des(key)

    def generate_text(self):
        text = "".join([random.choice(self.VALID_CHARS) for i in range(6)])
        seed = "".join(
            [random.choice(self.VALID_CHARS) for i in range(random.randint(5, 20))]
        )

        rV = self.PYDES.encrypt("{}:{}:{}".format(seed, time.time(), text), "*")
        rV = base64.urlsafe_b64encode(rV)
        rV = rV.decode()

        return rV

    def decode_text(self, text):
        decrypted_text = self.PYDES.decrypt(
            base64.urlsafe_b64decode(text.encode()), "*"
        )
        decrypted_text = decrypted_text.decode()
        return decrypted_text.split(":")[2]
