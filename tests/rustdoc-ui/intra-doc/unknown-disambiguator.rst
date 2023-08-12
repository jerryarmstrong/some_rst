tests/rustdoc-ui/intra-doc/unknown-disambiguator.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-test: "nightly|beta|1\.[0-9][0-9]\.[0-9]" -> "$$CHANNEL"
#![deny(warnings)]

//! Linking to [foo@banana] and [`bar@banana!()`].
//~^ ERROR unknown disambiguator `foo`
//~| ERROR unknown disambiguator `bar`
//! And to [no disambiguator](@nectarine) and [another](@apricot!()).
//~^ ERROR unknown disambiguator ``
//~| ERROR unknown disambiguator ``
//! And with weird backticks: [``foo@hello``] [foo`@`hello].
//~^ ERROR unknown disambiguator `foo`
//~| ERROR unknown disambiguator `foo`

fn main() {}


