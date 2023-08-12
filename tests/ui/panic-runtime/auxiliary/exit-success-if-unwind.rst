tests/ui/panic-runtime/auxiliary/exit-success-if-unwind.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic

#![crate_type = "rlib"]

struct Bomb;

impl Drop for Bomb {
    fn drop(&mut self) {
        std::process::exit(0);
    }
}

pub fn bar(f: fn()) {
    let _bomb = Bomb;
    f();
}


