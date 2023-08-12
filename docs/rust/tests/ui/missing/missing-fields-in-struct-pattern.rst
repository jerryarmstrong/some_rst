tests/ui/missing/missing-fields-in-struct-pattern.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S(usize, usize, usize, usize);

fn main() {
    if let S { a, b, c, d } = S(1, 2, 3, 4) {
    //~^ ERROR tuple variant `S` written as struct variant
        println!("hi");
    }
}


