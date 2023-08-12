tests/pretty/path-type-bounds.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact


trait Tr {
    fn dummy(&self) {}
}
impl Tr for isize {}

fn foo<'a>(x: Box<Tr + Sync + 'a>) -> Box<Tr + Sync + 'a> { x }

fn main() {
    let x: Box<Tr + Sync>;

    Box::new(1isize) as Box<Tr + Sync>;
}


