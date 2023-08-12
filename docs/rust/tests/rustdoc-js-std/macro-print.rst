tests/rustdoc-js-std/macro-print.js
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    const QUERY = 'macro:print';

const EXPECTED = {
    'others': [
        { 'path': 'std', 'name': 'print' },
        { 'path': 'std', 'name': 'println' },
        { 'path': 'std', 'name': 'eprint' },
        { 'path': 'std', 'name': 'eprintln' },
    ],
};


