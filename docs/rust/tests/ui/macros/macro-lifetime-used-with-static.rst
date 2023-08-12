tests/ui/macros/macro-lifetime-used-with-static.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
macro_rules! foo {
    ($l:lifetime) => {
        fn f(arg: &$l str) -> &$l str {
            arg
        }
    }
}

pub fn main() {
    foo!('static);
    let x: &'static str = f("hi");
    assert_eq!("hi", x);
}


