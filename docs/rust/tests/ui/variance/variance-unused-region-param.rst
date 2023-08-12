tests/ui/variance/variance-unused-region-param.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we report an error for unused type parameters in types.

struct SomeStruct<'a> { x: u32 } //~ ERROR parameter `'a` is never used
enum SomeEnum<'a> { Nothing } //~ ERROR parameter `'a` is never used
trait SomeTrait<'a> { fn foo(&self); } // OK on traits.

fn main() {}


