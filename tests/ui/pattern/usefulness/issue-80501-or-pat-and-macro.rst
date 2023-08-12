tests/ui/pattern/usefulness/issue-80501-or-pat-and-macro.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![deny(unreachable_patterns)]
pub enum TypeCtor {
    Slice,
    Array,
}

pub struct ApplicationTy(TypeCtor);

macro_rules! ty_app {
    ($ctor:pat) => {
        ApplicationTy($ctor)
    };
}

fn _foo(ty: ApplicationTy) {
    match ty {
        ty_app!(TypeCtor::Array) | ty_app!(TypeCtor::Slice) => {}
    }

    // same as above, with the macro expanded
    match ty {
        ApplicationTy(TypeCtor::Array) | ApplicationTy(TypeCtor::Slice) => {}
    }
}

fn main() {}


