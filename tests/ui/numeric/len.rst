tests/ui/numeric/len.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let array = [1, 2, 3];
    test(array.len()); //~ ERROR mismatched types
}

fn test(length: u32) {
    println!("{}", length);
}


