tests/ui/capture1.rs
====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: can't capture dynamic environment in a fn item

fn main() {
    let bar: isize = 5;
    fn foo() -> isize { return bar; }
}


