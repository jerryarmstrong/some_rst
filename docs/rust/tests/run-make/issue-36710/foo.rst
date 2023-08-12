tests/run-make/issue-36710/foo.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that linking to C++ code with global destructors works.

extern "C" {
    fn get() -> u32;
}

fn main() {
    let i = unsafe { get() };
    assert_eq!(i, 1234);
}


