tests/ui/typeck/typeck-fn-to-unsafe-fn-ptr.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// This tests reification from safe function to `unsafe fn` pointer

fn do_nothing() -> () {}

unsafe fn call_unsafe(func: unsafe fn() -> ()) -> () {
    func()
}

pub fn main() {
    unsafe { call_unsafe(do_nothing); }
}


