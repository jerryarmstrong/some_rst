tests/ui/specialization/specialization-overlap-hygiene.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

struct X;

macro_rules! define_f_legacy { () => {
    fn f() {}
}}
macro define_g_modern() {
    fn g() {}
}

impl X {
   fn f() {} //~ ERROR duplicate definitions with name `f`
   fn g() {} // OK
}
impl X {
    define_f_legacy!();
}
impl X {
    define_g_modern!();
}

fn main() {}


