tests/ui/rfc-2632-const-trait-impl/call-generic-method-chain.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Basic test for calling methods on generic type parameters in `const fn`.

// check-pass

#![feature(const_trait_impl)]

struct S;

impl const PartialEq for S {
    fn eq(&self, _: &S) -> bool {
        true
    }
    fn ne(&self, other: &S) -> bool {
        !self.eq(other)
    }
}

const fn equals_self<T: ~const PartialEq>(t: &T) -> bool {
    *t == *t
}

const fn equals_self_wrapper<T: ~const PartialEq>(t: &T) -> bool {
    equals_self(t)
}

pub const EQ: bool = equals_self_wrapper(&S);

fn main() {}


