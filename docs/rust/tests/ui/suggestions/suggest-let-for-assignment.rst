tests/ui/suggestions/suggest-let-for-assignment.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    demo = 1; //~ ERROR cannot find value `demo` in this scope
    dbg!(demo); //~ ERROR cannot find value `demo` in this scope

    x = "x"; //~ ERROR cannot find value `x` in this scope
    println!("x: {}", x); //~ ERROR cannot find value `x` in this scope

    if x == "x" {
        //~^ ERROR cannot find value `x` in this scope
        println!("x is 1");
    }

    y = 1 + 2; //~ ERROR cannot find value `y` in this scope
    println!("y: {}", y); //~ ERROR cannot find value `y` in this scope
}


