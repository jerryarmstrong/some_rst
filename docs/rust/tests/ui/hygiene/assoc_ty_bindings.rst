tests/ui/hygiene/assoc_ty_bindings.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// ignore-pretty pretty-printing is unhygienic

#![feature(decl_macro, associated_type_defaults)]

trait Base {
    type AssocTy;
    fn f();
}
trait Derived: Base {
    fn g();
}

macro mac() {
    type A = dyn Base<AssocTy = u8>;
    type B = dyn Derived<AssocTy = u8>;

    impl Base for u8 {
        type AssocTy = u8;
        fn f() {
            let _: Self::AssocTy;
        }
    }
    impl Derived for u8 {
        fn g() {
            let _: Self::AssocTy;
        }
    }

    fn h<T: Base, U: Derived>() {
        let _: T::AssocTy;
        let _: U::AssocTy;
    }
}

mac!();

fn main() {}


