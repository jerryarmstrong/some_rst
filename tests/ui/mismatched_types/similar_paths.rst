tests/ui/mismatched_types/similar_paths.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Option<T> {
    Some(T),
    None,
}

pub fn foo() -> Option<u8> {
    Some(42_u8)
    //~^ ERROR mismatched types [E0308]
}

fn main() {}


