client/dexterity/utils/random_hash.py
=====================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    import random
import string


def get_shared_random():
    return getattr(random, "_inst")


def random_hash(length=8, chars=string.ascii_uppercase + string.digits, seed=None):
    r = get_shared_random() if seed is None else random.Random(seed)
    return "".join(r.choice(chars) for _ in range(length))


