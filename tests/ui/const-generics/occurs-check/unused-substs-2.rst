tests/ui/const-generics/occurs-check/unused-substs-2.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

// The goal is to get an unevaluated const `ct` with a `Ty::Infer(TyVar(_#1t)` subst.
//
// If we are then able to infer `ty::Infer(TyVar(_#1t) := Ty<ct>` we introduced an
// artificial inference cycle.
struct Foo<const N: usize>;

trait Bind<T> {
    fn bind() -> (T, Self);
}

// `N` has to be `ConstKind::Unevaluated`.
impl<T> Bind<T> for Foo<{ 6 + 1 }> {
    fn bind() -> (T, Self) {
        (panic!(), Foo)
    }
}

fn main() {
    let (mut t, foo) = Foo::bind();
    // `t` is `ty::Infer(TyVar(_#1t))`
    // `foo` contains `ty::Infer(TyVar(_#1t))` in its substs
    t = foo;
    //~^ ERROR mismatched types
    //~| NOTE cyclic type
}


