tests/ui/traits/object/safety.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that static methods are not object-safe.

trait Tr {
    fn foo();
    fn bar(&self) { }
}

struct St;

impl Tr for St {
    fn foo() {}
}

fn main() {
    let _: &dyn Tr = &St; //~ ERROR E0038
    //~^ ERROR E0038
}


