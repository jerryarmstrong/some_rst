tests/ui/wf/wf-impl-self-type.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that we point at the proper location for an error
// involving the self-type of an impl

trait Foo {}
impl Foo for Option<[u8]> {} //~ ERROR the size for

fn main() {}


