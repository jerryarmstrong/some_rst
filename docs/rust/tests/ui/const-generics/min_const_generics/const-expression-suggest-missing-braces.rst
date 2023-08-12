tests/ui/const-generics/min_const_generics/const-expression-suggest-missing-braces.rs
=====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<const C: usize>() {}

const BAR: usize = 42;

fn a() {
    foo::<BAR + 3>(); //~ ERROR expected one of
}
fn b() {
    // FIXME(const_generics): these diagnostics are awful, because trait objects without `dyn` were
    // a terrible mistake.
    foo::<BAR + BAR>();
    //~^ ERROR expected trait, found constant `BAR`
    //~| ERROR expected trait, found constant `BAR`
    //~| ERROR type provided when a constant was expected
}
fn c() {
    foo::<3 + 3>(); //~ ERROR expressions must be enclosed in braces
}
fn d() {
    foo::<BAR - 3>(); //~ ERROR expected one of
}
fn e() {
    foo::<BAR - BAR>(); //~ ERROR expected one of
}
fn f() {
    foo::<100 - BAR>(); //~ ERROR expressions must be enclosed in braces
}
fn g() {
    foo::<bar<i32>()>(); //~ ERROR expected one of
}
fn h() {
    foo::<bar::<i32>()>(); //~ ERROR expected one of
}
fn i() {
    foo::<bar::<i32>() + BAR>(); //~ ERROR expected one of
}
fn j() {
    foo::<bar::<i32>() - BAR>(); //~ ERROR expected one of
}
fn k() {
    foo::<BAR - bar::<i32>()>(); //~ ERROR expected one of
}
fn l() {
    foo::<BAR - bar::<i32>()>(); //~ ERROR expected one of
}

const fn bar<const C: usize>() -> usize {
    C
}

fn main() {}


