tests/ui/generic-associated-types/issue-67510-pass.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: base extended
//[base] check-fail
//[extended] check-pass

#![cfg_attr(extended, feature(generic_associated_types_extended))]
#![cfg_attr(extended, allow(incomplete_features))]

trait X {
    type Y<'a>;
}

fn _func1<'a>(_x: Box<dyn X<Y<'a>=&'a ()>>) {}
//[base]~^ ERROR the trait `X` cannot be made into an object

fn main() {}


