tests/ui/traits/new-solver/fn-trait.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Ztrait-solver=next
// check-pass

fn require_fn(_: impl Fn() -> i32) {}

fn f() -> i32 {
    1i32
}

fn main() {
    require_fn(f);
    require_fn(f as fn() -> i32);
}


