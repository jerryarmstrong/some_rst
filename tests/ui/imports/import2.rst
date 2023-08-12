tests/ui/imports/import2.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use baz::zed::bar; //~ ERROR unresolved import `baz::zed` [E0432]
                   //~^ could not find `zed` in `baz`

mod baz {}
mod zed {
    pub fn bar() { println!("bar3"); }
}
fn main() {
    bar();
}


