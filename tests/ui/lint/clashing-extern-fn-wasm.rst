tests/ui/lint/clashing-extern-fn-wasm.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![crate_type = "lib"]

#[cfg(target_arch = "wasm32")]
mod wasm_non_clash {
    mod a {
        #[link(wasm_import_module = "a")]
        extern "C" {
            pub fn foo();
        }
    }

    mod b {
        #[link(wasm_import_module = "b")]
        extern "C" {
            pub fn foo() -> usize;
            // #79581: These declarations shouldn't clash because foreign fn names are mangled
            // on wasm32.
        }
    }
}


