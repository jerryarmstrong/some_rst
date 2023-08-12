tests/ui/consts/const-fn-in-vec.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    // should hint to create an inline `const` block
    // or to create a new `const` item
    let strings: [String; 5] = [String::new(); 5];
    //~^ ERROR the trait bound `String: Copy` is not satisfied
    println!("{:?}", strings);
}


