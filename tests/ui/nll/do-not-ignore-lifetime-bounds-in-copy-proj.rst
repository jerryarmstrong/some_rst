tests/ui/nll/do-not-ignore-lifetime-bounds-in-copy-proj.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the 'static bound from the Copy impl is respected. Regression test for #29149.

#[derive(Clone)]
struct Foo<'a>(&'a u32);
impl Copy for Foo<'static> {}

fn main() {
    let s = 2;
    let a = (Foo(&s),); //~ ERROR `s` does not live long enough [E0597]
    drop(a.0);
    drop(a.0);
}


