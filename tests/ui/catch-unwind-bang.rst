tests/ui/catch-unwind-bang.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// needs-unwind

fn worker() -> ! {
    panic!()
}

fn main() {
    std::panic::catch_unwind(worker).unwrap_err();
}


