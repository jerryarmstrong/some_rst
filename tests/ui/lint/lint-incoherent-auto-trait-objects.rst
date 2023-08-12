tests/ui/lint/lint-incoherent-auto-trait-objects.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {}

impl Foo for dyn Send {}

impl Foo for dyn Send + Send {}
//~^ ERROR conflicting implementations
//~| hard error

impl Foo for dyn Send + Sync {}

impl Foo for dyn Sync + Send {}
//~^ ERROR conflicting implementations
//~| hard error

impl Foo for dyn Send + Sync + Send {}
//~^ ERROR conflicting implementations
//~| hard error

fn main() {}


