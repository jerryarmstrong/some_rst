tests/ui/closures/2229_closure_analysis/issue-92724-needsdrop-query-cycle.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ICEs if checking if there is a significant destructor causes a query cycle
// check-pass

#![warn(rust_2021_incompatible_closure_captures)]
pub struct Foo(Bar);
pub struct Bar(Baz);
pub struct Baz(Vec<Foo>);

impl Foo {
    pub fn baz(self, v: Baz) -> Baz {
        (|| v)()
    }
}
fn main() {}


