tests/ui/mismatched_types/numeric-literal-cast.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(_: u16) {}
fn foo1(_: f64) {}
fn foo2(_: i32) {}

fn main() {
    foo(1u8);
//~^ ERROR mismatched types
    foo1(2f32);
//~^ ERROR mismatched types
    foo2(3i16);
//~^ ERROR mismatched types
}


