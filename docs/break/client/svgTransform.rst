client/svgTransform.js
======================

Last edited: 2022-06-08 08:09:30

Contents:

.. code-block:: js

    module.exports = {
  process(): string {
    return "module.exports = {};";
  },
  getCacheKey(): string {
    // The output is always the same.
    return "svgTransform";
  },
};


