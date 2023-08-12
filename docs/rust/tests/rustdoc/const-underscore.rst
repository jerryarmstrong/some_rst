tests/rustdoc/const-underscore.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --document-private-items

// @!has const_underscore/constant._.html
const _: () = {
    #[no_mangle]
    extern "C" fn implementation_detail() {}
};


