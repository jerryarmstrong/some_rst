tests/rustdoc-js-std/alias-2.js
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    const QUERY = '+';

const EXPECTED = {
    'others': [
        { 'path': 'std::ops', 'name': 'AddAssign' },
        { 'path': 'std::ops', 'name': 'Add' },
        { 'path': 'core::ops', 'name': 'AddAssign' },
        { 'path': 'core::ops', 'name': 'Add' },
    ],
};


