tests/rustdoc-js-std/return-specific.js
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    const QUERY = 'struct:string';

const EXPECTED = {
    'in_args': [
        { 'path': 'std::string::String', 'name': 'ne' },
    ],
    'returned': [
        { 'path': 'std::string::String', 'name': 'add' },
    ],
};


