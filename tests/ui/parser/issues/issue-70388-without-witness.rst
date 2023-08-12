tests/ui/parser/issues/issue-70388-without-witness.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// This is for checking if we can apply suggestions as-is.

pub struct Foo(#[allow(unused_tuple_struct_fields)] i32);

fn main() {
    let Foo(...) = Foo(0); //~ ERROR unexpected `...`
    let [_, ..., _] = [0, 1]; //~ ERROR unexpected `...`
}


