tests/ui/rfc-2632-const-trait-impl/impl-with-default-fn-fail.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

#[const_trait]
trait Tr {
    fn req(&self);

    fn default() {}
}

struct S;

impl const Tr for u16 {
    fn default() {}
} //~^^ ERROR not all trait items implemented


fn main() {}


