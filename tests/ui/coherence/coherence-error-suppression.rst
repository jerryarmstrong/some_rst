tests/ui/coherence/coherence-error-suppression.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check that error types in coherence do not cause error cascades.

trait Foo {}

impl Foo for i8 {}
impl Foo for i16 {}
impl Foo for i32 {}
impl Foo for i64 {}
impl Foo for DoesNotExist {}
//~^ ERROR E0412
impl Foo for u8 {}
impl Foo for u16 {}
impl Foo for u32 {}
impl Foo for u64 {}

fn main() {}


