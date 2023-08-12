tests/ui/type/type-shadow.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    type X = isize;
    type Y = X;
    if true {
        type X = &'static str;
        let y: Y = "hello"; //~ ERROR mismatched types
    }
}


