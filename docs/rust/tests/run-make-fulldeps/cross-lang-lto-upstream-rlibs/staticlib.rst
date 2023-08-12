tests/run-make-fulldeps/cross-lang-lto-upstream-rlibs/staticlib.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="staticlib"]

extern crate upstream;

#[no_mangle]
pub extern "C" fn bar() {
    upstream::foo();
}


