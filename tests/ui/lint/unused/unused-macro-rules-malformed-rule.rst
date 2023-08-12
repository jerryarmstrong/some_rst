tests/ui/lint/unused/unused-macro-rules-malformed-rule.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused_macro_rules)]

macro_rules! foo {
    (v) => {};
    (w) => {};
    () => 0; //~ ERROR: macro rhs must be delimited
}

fn main() {
    foo!(v);
}


