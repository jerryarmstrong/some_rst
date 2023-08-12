tests/ui/issues/issue-4972.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_patterns)]

trait MyTrait {
    fn dummy(&self) {}
}

pub enum TraitWrapper {
    A(Box<dyn MyTrait + 'static>),
}

fn get_tw_map(tw: &TraitWrapper) -> &dyn MyTrait {
    match *tw {
        TraitWrapper::A(box ref map) => map, //~ ERROR cannot be dereferenced
    }
}

pub fn main() {}


