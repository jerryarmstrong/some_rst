tests/rustdoc-js-std/deduplication.js
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    // ignore-order

const QUERY = 'is_nan';

const EXPECTED = {
    'others': [
        { 'path': 'std::f32', 'name': 'is_nan' },
        { 'path': 'std::f64', 'name': 'is_nan' },
        { 'path': 'std::option::Option', 'name': 'is_none' },
    ],
};


