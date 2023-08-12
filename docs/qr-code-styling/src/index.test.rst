src/index.test.js
=================

Last edited: 2023-05-04 20:47:44

Contents:

.. code-block:: js

    import * as index from "./index";

describe("Index", () => {
  it.each(["dotTypes", "errorCorrectionLevels", "errorCorrectionPercents", "modes", "qrTypes", "default"])(
    "The module should export certain submodules",
    (moduleName) => {
      expect(Object.keys(index)).toContain(moduleName);
    }
  );
});


