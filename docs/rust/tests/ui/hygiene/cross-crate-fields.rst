tests/ui/hygiene/cross-crate-fields.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that fields on a struct defined in another crate are resolved correctly
// their names differ only in `SyntaxContext`.

// run-pass
// aux-build:fields.rs

extern crate fields;

use fields::*;

fn main() {
    check_fields_local();

    test_fields!(check_fields);
    test_fields2!(check_fields);

    let s1 = test_fields!(construct);
    check_fields(s1);
    test_fields!(check_fields_of s1);

    let s2 = test_fields2!(construct);
    check_fields(s2);
    test_fields2!(check_fields_of s2);
}


