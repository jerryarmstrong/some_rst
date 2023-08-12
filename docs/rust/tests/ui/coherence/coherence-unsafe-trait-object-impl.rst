tests/ui/coherence/coherence-unsafe-trait-object-impl.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that unsafe trait object do not implement themselves
// automatically

#![feature(object_safe_for_dispatch)]

trait Trait: Sized {
    fn call(&self);
}

fn takes_t<S: Trait>(s: S) {
    s.call();
}

fn takes_t_obj(t: &dyn Trait) {
    takes_t(t); //~ ERROR E0277
}

fn main() {}


