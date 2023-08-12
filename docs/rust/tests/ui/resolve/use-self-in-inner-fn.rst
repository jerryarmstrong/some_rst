tests/ui/resolve/use-self-in-inner-fn.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A;

impl A {
//~^ NOTE `Self` type implicitly declared here, by this `impl`
    fn banana(&mut self) {
        fn peach(this: &Self) {
        //~^ ERROR can't use generic parameters from outer function
        //~| NOTE use of generic parameter from outer function
        //~| NOTE use a type here instead
        }
    }
}

fn main() {}


