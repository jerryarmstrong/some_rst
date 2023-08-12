tests/ui/type-inference/sort_by_key.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut lst: [([i32; 10], bool); 10] = [([0; 10], false); 10];
    lst.sort_by_key(|&(v, _)| v.iter().sum()); //~ ERROR type annotations needed
    println!("{:?}", lst);
}


