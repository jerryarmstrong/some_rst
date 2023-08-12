tests/ui/impl-trait/in-trait/foreign.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build: rpitit.rs

extern crate rpitit;

fn main() {
    // Witness an RPITIT from another crate
    let () = <rpitit::Foreign as rpitit::Foo>::bar();
}


