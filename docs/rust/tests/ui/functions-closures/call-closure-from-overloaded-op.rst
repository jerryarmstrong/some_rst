tests/ui/functions-closures/call-closure-from-overloaded-op.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn foo() -> isize { 22 }

pub fn main() {
    let mut x: Vec<extern "Rust" fn() -> isize> = Vec::new();
    x.push(foo);
    assert_eq!((x[0])(), 22);
}


