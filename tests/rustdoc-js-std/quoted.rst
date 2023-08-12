tests/rustdoc-js-std/quoted.js
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    // ignore-order

const QUERY = '"error"';
const FILTER_CRATE = 'std';

const EXPECTED = {
    'others': [
        { 'path': 'std', 'name': 'error' },
        { 'path': 'std::fmt', 'name': 'Error' },
        { 'path': 'std::io', 'name': 'Error' },
    ],
    'in_args': [
        { 'path': 'std::fmt::Error', 'name': 'eq' },
        { 'path': 'std::fmt::Error', 'name': 'cmp' },
        { 'path': 'std::fmt::Error', 'name': 'partial_cmp' },

    ],
    'returned': [
        { 'path': 'std::fmt::LowerExp', 'name': 'fmt' },
    ],
};


