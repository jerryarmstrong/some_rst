tests/ui/nll/normalization-bounds.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that lifetime bounds get checked the right way around with NLL enabled.

// check-pass

trait Visitor<'d> {
    type Value;
}

impl<'a, 'd: 'a> Visitor<'d> for &'a () {
    type Value = ();
}

fn visit_seq<'d: 'a, 'a>() -> <&'a () as Visitor<'d>>::Value {}

fn main() {}


