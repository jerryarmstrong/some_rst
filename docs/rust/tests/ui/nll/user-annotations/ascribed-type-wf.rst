tests/ui/nll/user-annotations/ascribed-type-wf.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #101350.
// check-fail

trait Trait {
    type Ty;
}

impl Trait for &'static () {
    type Ty = ();
}

fn extend<'a>() {
    None::<<&'a () as Trait>::Ty>;
    //~^ ERROR lifetime may not live long enough
}

fn main() {}


