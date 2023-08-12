tests/run-make-fulldeps/sanitizer-cdylib-link/program.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    fn overflow();
}

fn main() {
    unsafe { overflow() }
}


