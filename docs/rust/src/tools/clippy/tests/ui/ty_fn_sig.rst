src/tools/clippy/tests/ui/ty_fn_sig.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test

pub fn retry<F: Fn()>(f: F) {
    for _i in 0.. {
        f();
    }
}

fn main() {
    for y in 0..4 {
        let func = || ();
        func();
    }
}


