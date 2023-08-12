tests/ui/unsafe/unsafe-subtyping.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that safe fns are not a subtype of unsafe fns.

fn foo(x: Option<fn(i32)>) -> Option<unsafe fn(i32)> {
    x //~ ERROR mismatched types
}

fn bar(x: fn(i32)) -> unsafe fn(i32) {
    x // OK, coercion!
}

fn main() { }


