tests/ui/attributes/doc-attr.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![deny(warnings)]
#![doc(as_ptr)]
//~^ ERROR unknown `doc` attribute
//~^^ WARN

#[doc(as_ptr)]
//~^ ERROR unknown `doc` attribute
//~^^ WARN
pub fn foo() {}

#[doc(123)]
//~^ ERROR invalid `doc` attribute
//~| WARN
#[doc("hello", "bar")]
//~^ ERROR invalid `doc` attribute
//~| WARN
//~| ERROR invalid `doc` attribute
//~| WARN
#[doc(foo::bar, crate::bar::baz = "bye")]
//~^ ERROR unknown `doc` attribute
//~| WARN
//~| ERROR unknown `doc` attribute
//~| WARN
fn bar() {}


