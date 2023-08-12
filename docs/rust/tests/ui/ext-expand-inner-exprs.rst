tests/ui/ext-expand-inner-exprs.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

static FOO : &'static str = concat!(concat!("hel", "lo"), "world");

pub fn main() {
    assert_eq!(FOO, "helloworld");
}


