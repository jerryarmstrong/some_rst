tests/ui/lint/force-warn/lint-group-allowed-lint-group.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // --force-warn $LINT_GROUP causes $LINT to warn despite
// $LINT_GROUP being allowed in module
// compile-flags: --force-warn rust_2018_idioms
// check-pass

#![allow(rust_2018_idioms)]

pub trait SomeTrait {}

pub fn function(_x: Box<SomeTrait>) {}
//~^ WARN trait objects without an explicit `dyn` are deprecated
//~| WARN this is accepted in the current edition
//~| WARN trait objects without an explicit `dyn` are deprecated
//~| WARN this is accepted in the current edition
//~| WARN trait objects without an explicit `dyn` are deprecated
//~| WARN this is accepted in the current edition

fn main() {}


