tests/rustdoc-js-std/basic.js
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    const QUERY = 'String';

const EXPECTED = {
    'others': [
        { 'path': 'std::string', 'name': 'String' },
        { 'path': 'std::ffi', 'name': 'CString' },
        { 'path': 'std::ffi', 'name': 'OsString' },
    ],
    'in_args': [
        { 'path': 'std::str', 'name': 'eq' },
    ],
    'returned': [
        { 'path': 'std::string::String', 'name': 'add' },
    ],
};


