tests/ui/typeck/typeck-closure-to-unsafe-fn-ptr.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

unsafe fn call_unsafe(func: unsafe fn() -> ()) -> () {
    func()
}

pub fn main() {
    unsafe { call_unsafe(|| {}); }
}


