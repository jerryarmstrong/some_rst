tests/rustdoc-js-std/path-ordering.js
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    const QUERY = 'hashset::insert';

const EXPECTED = {
    'others': [
        // ensure hashset::insert comes first
        { 'path': 'std::collections::hash_set::HashSet', 'name': 'insert' },
        { 'path': 'std::collections::hash_set::HashSet', 'name': 'get_or_insert' },
        { 'path': 'std::collections::hash_set::HashSet', 'name': 'get_or_insert_with' },
        { 'path': 'std::collections::hash_set::HashSet', 'name': 'get_or_insert_owned' },
        { 'path': 'std::collections::hash_map::HashMap', 'name': 'insert' },
    ],
};


