tests/ui/borrowck/borrowck-thread-local-static-borrow-outlives-fn.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(thread_local)]

#[thread_local]
static FOO: u8 = 3;

fn assert_static(_t: &'static u8) {}
fn main() {
     assert_static(&FOO); //~ ERROR [E0712]
}


