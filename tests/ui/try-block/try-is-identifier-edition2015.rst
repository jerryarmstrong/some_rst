tests/ui/try-block/try-is-identifier-edition2015.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(non_camel_case_types)]
// compile-flags: --edition 2015

fn main() {
    let try = 2;
    struct try { try: u32 }
    let try: try = try { try };
    assert_eq!(try.try, 2);
}


