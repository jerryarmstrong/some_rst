src/tools/miri/tests/fail/abort-terminator.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(c_unwind)]

extern "C" fn panic_abort() {
    //~^ ERROR: the program aborted
    panic!()
}

fn main() {
    panic_abort();
}


