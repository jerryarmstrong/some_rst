tests/ui/parser/variadic-ffi-nested-syntactic-fail.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f1<'a>(x: u8, y: &'a ...) {}
//~^ ERROR C-variadic type `...` may not be nested inside another type

fn f2<'a>(x: u8, y: Vec<&'a ...>) {}
//~^ ERROR C-variadic type `...` may not be nested inside another type

fn main() {
    let _recovery_witness: () = 0; //~ ERROR mismatched types
}


