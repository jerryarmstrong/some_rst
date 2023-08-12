tests/ui/proc-macro/attr-on-trait.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:attr-on-trait.rs

extern crate attr_on_trait;

use attr_on_trait::foo;

trait Foo {
    #[foo]
    fn foo() {}
}

impl Foo for i32 {
    fn foo(&self) {}
}

fn main() {
    3i32.foo();
}


