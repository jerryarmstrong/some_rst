src/tools/clippy/tests/ui/unknown_clippy_lints.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::pedantic)]
// Should suggest lowercase
#![allow(clippy::All)]
#![warn(clippy::CMP_NAN)]

// Should suggest similar clippy lint name
#[warn(clippy::if_not_els)]
#[warn(clippy::UNNecsaRy_cAst)]
#[warn(clippy::useles_transute)]
// Shouldn't suggest rustc lint name(`dead_code`)
#[warn(clippy::dead_cod)]
// Shouldn't suggest removed/deprecated clippy lint name(`unused_collect`)
#[warn(clippy::unused_colle)]
// Shouldn't suggest renamed clippy lint name(`const_static_lifetime`)
#[warn(clippy::const_static_lifetim)]
fn main() {}


