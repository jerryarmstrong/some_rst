tests/ui/unknown-lint-tool-name.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(foo::bar)] //~ ERROR unknown tool name `foo` found in scoped lint: `foo::bar`
                   //~| ERROR unknown tool name `foo` found in scoped lint: `foo::bar`

#[allow(foo::bar)] //~ ERROR unknown tool name `foo` found in scoped lint: `foo::bar`
                   //~| ERROR unknown tool name `foo` found in scoped lint: `foo::bar`
fn main() {}


