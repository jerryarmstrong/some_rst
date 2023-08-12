tests/run-make/issue-47384/lib.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    #[link_section = ".rodata.STATIC"]
    #[used]
    static STATIC: [u32; 10] = [1; 10];
}

mod bar {
    #[no_mangle]
    extern "C" fn bar() -> i32 {
        0
    }
}


