tests/ui/privacy/private-inferred-type-1.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Arr0 {
    fn arr0_secret(&self);
}
trait TyParam {
    fn ty_param_secret(&self);
}

mod m {
    struct Priv;

    impl ::Arr0 for [Priv; 0] { fn arr0_secret(&self) {} }
    impl ::TyParam for Option<Priv> { fn ty_param_secret(&self) {} }
}

fn main() {
    [].arr0_secret(); //~ ERROR type `Priv` is private
    None.ty_param_secret(); //~ ERROR type `Priv` is private
}


