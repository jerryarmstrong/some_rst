tests/run-make/const_fn_mir/main.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // emit-mir
// check-pass

const fn foo() -> i32 {
    5 + 6
}

fn main() {
    foo();
}


