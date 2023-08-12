tests/run-make-fulldeps/redundant-libs/main.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    fn bar();
    fn baz();
}

fn main() {
    unsafe {
        bar();
        baz();
    }
}


