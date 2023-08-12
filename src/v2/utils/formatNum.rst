src/v2/utils/formatNum.js
=========================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    export default function formatNum(val) {
  if (!val) return 0;
  return val.toLocaleString();
}


