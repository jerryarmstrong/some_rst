tests/rustdoc-js-std/vec-new.js
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    const QUERY = 'Vec::new';

const EXPECTED = {
    'others': [
        { 'path': 'std::vec::Vec', 'name': 'new' },
        { 'path': 'alloc::vec::Vec', 'name': 'new' },
        { 'path': 'std::vec::Vec', 'name': 'new_in' },
        { 'path': 'alloc::vec::Vec', 'name': 'new_in' },
    ],
};


