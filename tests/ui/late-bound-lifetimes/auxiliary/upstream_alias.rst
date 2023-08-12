tests/ui/late-bound-lifetimes/auxiliary/upstream_alias.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Trait<'a> {
    type Assoc;
}

pub type Alias<'a, T> = <T as Trait<'a>>::Assoc;


