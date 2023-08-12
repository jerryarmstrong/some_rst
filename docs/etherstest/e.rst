e.js
====

Last edited: 2023-07-23 17:13:40

Contents:

.. code-block:: js

    import * as ethers from "ethers";
import { pbkdf2Sync } from "react-native-quick-crypto";

ethers.pbkdf2.register(
  (
    password,
    salt,
    iterations,
    keylen,
    algo
  ) => {
    return ethers.hexlify(pbkdf2Sync(password, salt, iterations, keylen, algo));
  }
);

export * from "ethers";


