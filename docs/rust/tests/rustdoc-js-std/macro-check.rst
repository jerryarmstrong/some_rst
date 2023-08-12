tests/rustdoc-js-std/macro-check.js
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    // ignore-order

const QUERY = 'panic';

const EXPECTED = {
    'others': [
        { 'path': 'std', 'name': 'panic', ty: 14 }, // 15 is for macros
        { 'path': 'std', 'name': 'panic', ty: 0 }, // 0 is for modules
    ],
};


