tests/ui/suggestions/crate-or-module-typo.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

use st::cell::Cell; //~ ERROR failed to resolve: use of undeclared crate or module `st`

mod bar {
    pub fn bar() { bar::baz(); } //~ ERROR failed to resolve: use of undeclared crate or module `bar`

    fn baz() {}
}

use bas::bar; //~ ERROR unresolved import `bas`

struct Foo {
    bar: st::cell::Cell<bool> //~ ERROR failed to resolve: use of undeclared crate or module `st`
}

fn main() {}


