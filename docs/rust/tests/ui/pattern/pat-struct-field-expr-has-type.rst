tests/ui/pattern/pat-struct-field-expr-has-type.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    f: u8,
}

fn main() {
    match (S { f: 42 }) {
        S { f: Ok(_) } => {} //~ ERROR mismatched types
    }
}


