tests/ui/proc-macro/attribute-spans-preserved.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:attribute-spans-preserved.rs

extern crate attribute_spans_preserved as foo;

use foo::foo;

#[ foo ( let y: u32 = "z"; ) ] //~ ERROR: mismatched types
#[ bar { let x: u32 = "y"; } ] //~ ERROR: mismatched types
fn main() {
}


