tests/run-make/native-link-modifier-bundle/non-bundled.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[link(name = "native-staticlib", kind = "static", modifiers = "-bundle")]
extern "C" {
    pub fn native_func();
}

#[no_mangle]
pub extern "C" fn wrapped_func() {
    unsafe {
        native_func();
    }
}


