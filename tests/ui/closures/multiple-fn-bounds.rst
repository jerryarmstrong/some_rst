tests/ui/closures/multiple-fn-bounds.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<F: Fn(&char) -> bool + Fn(char) -> bool>(f: F) {
    //~^ NOTE required by a bound in `foo`
    //~| NOTE required by this bound in `foo`
    //~| NOTE closure inferred to have a different signature due to this bound
    todo!();
}

fn main() {
    let v = true;
    foo(move |x| v);
    //~^ ERROR type mismatch in closure arguments
    //~| NOTE expected closure signature
    //~| NOTE expected due to this
    //~| NOTE found signature defined here
}


