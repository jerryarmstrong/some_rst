src/tools/miri/tests/fail/extern_static.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Even referencing an unknown `extern static` already triggers an error.

extern "C" {
    static mut FOO: i32;
}

fn main() {
    let _val = unsafe { std::ptr::addr_of!(FOO) }; //~ ERROR: is not supported by Miri
}


