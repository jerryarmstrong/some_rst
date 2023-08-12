tests/rustdoc-js-std/typed-query.js
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    // exact-check

const QUERY = 'macro:print';
const FILTER_CRATE = 'std';

const EXPECTED = {
    'others': [
        { 'path': 'std', 'name': 'print' },
        { 'path': 'std', 'name': 'println' },
        { 'path': 'std', 'name': 'eprint' },
        { 'path': 'std', 'name': 'eprintln' },
        { 'path': 'std::pin', 'name': 'pin' },
        { 'path': 'std::future', 'name': 'join' },
        { 'path': 'std', 'name': 'line' },
        { 'path': 'std', 'name': 'write' },
    ],
};


