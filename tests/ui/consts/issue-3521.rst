tests/ui/consts/issue-3521.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() {
    #[allow(non_upper_case_globals)]
    let foo: isize = 100;

    #[derive(Debug)]
    enum Stuff {
        Bar = foo
        //~^ ERROR attempt to use a non-constant value in a constant
    }

    println!("{:?}", Stuff::Bar);
}


