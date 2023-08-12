src/v2/utils/getAvatarIndex.js
==============================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {random} from 'lodash/fp';

export default function getAvatarIndex(key) {
  if (!key) return random(0, 9);
  const utf8Encode = new TextEncoder();
  const [index] = utf8Encode.encode(key);
  return index % 10;
}


