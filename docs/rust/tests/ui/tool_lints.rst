tests/ui/tool_lints.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[warn(foo::bar)]
//~^ ERROR unknown tool name `foo` found in scoped lint: `foo::bar`
//~| ERROR unknown tool name `foo` found in scoped lint: `foo::bar`
fn main() {}


