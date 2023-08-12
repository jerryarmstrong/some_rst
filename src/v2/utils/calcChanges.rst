src/v2/utils/calcChanges.js
===========================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    // @flow

export default (oldValue: string | number, newValue: string | number) => {
  if (!oldValue || !newValue) {
    return 0;
  }
  return ((+newValue * 100) / (+oldValue || 1) - 100).toFixed(2);
};


