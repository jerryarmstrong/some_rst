tests/ui/span/typo-suggestion.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let foo = 1;

    // `foo` shouldn't be suggested, it is too dissimilar from `bar`.
    println!("Hello {}", bar); //~ ERROR cannot find value

    // But this is close enough.
    println!("Hello {}", fob); //~ ERROR cannot find value
}


