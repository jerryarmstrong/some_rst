tests/ui/macros/macro-lifetime-used-with-bound.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
macro_rules! foo {
    ($l:lifetime, $l2:lifetime) => {
        fn f<$l: $l2, $l2>(arg: &$l str, arg2: &$l2 str) -> &$l str {
            arg
        }
    }
}

pub fn main() {
    foo!('a, 'b);
    let x: &'static str = f("hi", "there");
    assert_eq!("hi", x);
}


