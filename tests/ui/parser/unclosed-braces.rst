tests/ui/parser/unclosed-braces.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    x: [usize; 3],
}

fn foo() {
    {
        {
            println!("hi");
        }
    }
}

fn main() {
//~^ NOTE unclosed delimiter
    {
        {
        //~^ NOTE this delimiter might not be properly closed...
            foo();
    }
    //~^ NOTE ...as it matches this but it has different indentation
}
//~ ERROR this file contains an unclosed delimiter


