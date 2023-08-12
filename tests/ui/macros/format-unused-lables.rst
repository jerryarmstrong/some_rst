tests/ui/macros/format-unused-lables.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    println!("Test", 123, 456, 789);
    //~^ ERROR multiple unused formatting arguments

    println!("Test2",
        123,  //~ ERROR multiple unused formatting arguments
        456,
        789
    );

    println!("Some stuff", UNUSED="args"); //~ ERROR named argument never used

    println!("Some more $STUFF",
        "woo!",  //~ ERROR multiple unused formatting arguments
            STUFF=
       "things"
             , UNUSED="args");
}


