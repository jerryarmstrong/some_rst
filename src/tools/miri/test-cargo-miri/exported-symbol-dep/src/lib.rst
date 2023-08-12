src/tools/miri/test-cargo-miri/exported-symbol-dep/src/lib.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
fn exported_symbol() -> i32 {
    123456
}

struct AssocFn;

impl AssocFn {
    #[no_mangle]
    fn assoc_fn_as_exported_symbol() -> i32 {
        -123456
    }
}


