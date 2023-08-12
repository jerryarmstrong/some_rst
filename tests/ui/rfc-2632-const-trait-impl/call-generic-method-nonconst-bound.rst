tests/ui/rfc-2632-const-trait-impl/call-generic-method-nonconst-bound.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct S;

impl PartialEq for S {
    fn eq(&self, _: &S) -> bool {
        true
    }
}

const fn equals_self<T: PartialEq>(t: &T) -> bool {
    true
}

pub const EQ: bool = equals_self(&S);

fn main() {}


