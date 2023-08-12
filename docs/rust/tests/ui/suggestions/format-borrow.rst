tests/ui/suggestions/format-borrow.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a: String = &String::from("a");
    //~^ ERROR mismatched types
    let b: String = &format!("b");
    //~^ ERROR mismatched types
    let c: String = &mut format!("c");
    //~^ ERROR mismatched types
    let d: String = &mut (format!("d"));
    //~^ ERROR mismatched types
}


