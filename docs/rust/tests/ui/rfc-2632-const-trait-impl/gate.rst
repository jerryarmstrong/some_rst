tests/ui/rfc-2632-const-trait-impl/gate.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-const_closures
fn main() {
    (const || {})();
    //~^ ERROR: const closures are experimental
}


