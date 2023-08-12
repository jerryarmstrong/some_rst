tests/run-make-fulldeps/sanitizer-staticlib-link/program.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[link(name = "library")]
extern "C" {
    fn overflow();
}

fn main() {
    unsafe {
        overflow();
    }
}


