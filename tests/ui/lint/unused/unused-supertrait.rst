tests/ui/lint/unused/unused-supertrait.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused_must_use)]

fn it() -> impl ExactSizeIterator<Item = ()> {
    let x: Box<dyn ExactSizeIterator<Item = ()>> = todo!();
    x
}

fn main() {
    it();
    //~^ ERROR unused implementer of `Iterator` that must be used
}


