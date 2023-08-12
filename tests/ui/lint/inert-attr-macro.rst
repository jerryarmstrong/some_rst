tests/ui/lint/inert-attr-macro.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![warn(unused)]

macro_rules! foo {
    () => {}
}

fn main() {
    #[inline] foo!(); //~ WARN unused attribute `inline`

    // This does nothing, since `#[allow(warnings)]` is itself
    // an inert attribute on a macro call
    #[allow(warnings)] #[inline] foo!(); //~ WARN unused attribute `allow`
    //~^ WARN unused attribute `inline`

    // This does work, since the attribute is on a parent
    // of the macro invocation.
    #[allow(warnings)] { #[inline] foo!(); }
}


