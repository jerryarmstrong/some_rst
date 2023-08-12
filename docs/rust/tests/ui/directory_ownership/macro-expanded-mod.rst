tests/ui/directory_ownership/macro-expanded-mod.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that macro-expanded non-inline modules behave correctly

macro_rules! mod_decl {
    ($i:ident) => {
        mod $i; //~ ERROR cannot declare a non-inline module inside a block
    };
}

mod macro_expanded_mod_helper {
    mod_decl!(foo); // This should search in the folder `macro_expanded_mod_helper`
}

fn main() {
    mod_decl!(foo);
}


