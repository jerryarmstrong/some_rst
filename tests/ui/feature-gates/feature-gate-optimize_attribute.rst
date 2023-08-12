tests/ui/feature-gates/feature-gate-optimize_attribute.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="rlib"]
#![optimize(speed)] //~ ERROR the `#[optimize]` attribute is an experimental feature

#[optimize(size)] //~ ERROR the `#[optimize]` attribute is an experimental feature
mod module {

#[optimize(size)] //~ ERROR the `#[optimize]` attribute is an experimental feature
fn size() {}

#[optimize(speed)] //~ ERROR the `#[optimize]` attribute is an experimental feature
fn speed() {}

#[optimize(banana)]
//~^ ERROR the `#[optimize]` attribute is an experimental feature
//~| ERROR E0722
fn not_known() {}

}


