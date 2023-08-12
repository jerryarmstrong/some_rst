tests/ui/consts/control-flow/try.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // The `?` operator is still not const-evaluatable because it calls `From::from` on the error
// variant.

const fn opt() -> Option<i32> {
    let x = Some(2);
    x?; //~ ERROR `?` is not allowed in a `const fn`
    None
}

fn main() {}


