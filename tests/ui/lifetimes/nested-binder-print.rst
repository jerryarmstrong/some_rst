tests/ui/lifetimes/nested-binder-print.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct TwoLt<'a, 'b>(&'a (), &'b ());
type Foo<'a> = fn(TwoLt<'_, 'a>);

fn foo() {
    let y: for<'a> fn(Foo<'a>);
    let x: u32 = y;
    //~^ ERROR mismatched types
}

fn main() {}


