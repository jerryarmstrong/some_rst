tests/ui/suggestions/dont-wrap-ambiguous-receivers.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod banana {
    //~^ HELP the following traits are implemented but not in scope
    pub struct Chaenomeles;

    pub trait Apple {
        fn pick(&self) {}
    }
    impl Apple for Chaenomeles {}

    pub trait Peach {
        fn pick(&self, a: &mut ()) {}
    }
    impl<Mango: Peach> Peach for Box<Mango> {}
    impl Peach for Chaenomeles {}
}

fn main() {
    banana::Chaenomeles.pick()
    //~^ ERROR no method named
    //~| HELP items from traits can only be used if the trait is in scope
}


