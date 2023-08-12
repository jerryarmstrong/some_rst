tests/ui/consts/dangling_raw_ptr.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const FOO: *const u32 = { //~ ERROR encountered dangling pointer in final constant
    let x = 42;
    &x
};

fn main() {
    let x = FOO;
}


