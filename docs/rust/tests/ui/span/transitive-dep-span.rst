tests/ui/span/transitive-dep-span.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that we properly serialize/deserialize spans from transitive dependencies
// (e.g. imported SourceFiles)
//
// The order of these next lines is important, since we need
// transitive_dep_two.rs to be able to reference transitive_dep_three.rs
//
// aux-build: transitive_dep_three.rs
// aux-build: transitive_dep_two.rs
// compile-flags: -Z macro-backtrace

extern crate transitive_dep_two;

transitive_dep_two::parse_error!(); //~ ERROR expected one of

fn main() {}


