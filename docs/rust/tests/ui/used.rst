tests/ui/used.rs
================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[used]
static FOO: u32 = 0; // OK

#[used] //~ ERROR attribute must be applied to a `static` variable
fn foo() {}

#[used] //~ ERROR attribute must be applied to a `static` variable
struct Foo {}

#[used] //~ ERROR attribute must be applied to a `static` variable
trait Bar {}

#[used] //~ ERROR attribute must be applied to a `static` variable
impl Bar for Foo {}

fn main() {}


