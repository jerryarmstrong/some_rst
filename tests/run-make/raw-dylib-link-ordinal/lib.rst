tests/run-make/raw-dylib-link-ordinal/lib.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![cfg_attr(target_arch = "x86", feature(raw_dylib))]

#[link(name = "exporter", kind = "raw-dylib")]
extern {
    #[link_ordinal(13)]
    fn imported_function();
    #[link_ordinal(5)]
    static mut imported_variable: i32;
    #[link_ordinal(9)]
    fn print_imported_variable();
}

pub fn library_function() {
    unsafe {
        imported_function();
        imported_variable = 42;
        print_imported_variable();
        imported_variable = -42;
        print_imported_variable();
    }
}


