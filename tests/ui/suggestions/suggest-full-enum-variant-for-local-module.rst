tests/ui/suggestions/suggest-full-enum-variant-for-local-module.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod option {
    pub enum O<T> {
        Some(T),
        None,
    }
}

fn main() {
    let _: option::O<()> = (); //~ ERROR 9:28: 9:30: mismatched types [E0308]
}


