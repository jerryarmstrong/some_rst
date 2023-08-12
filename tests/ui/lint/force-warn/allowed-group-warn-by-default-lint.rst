tests/ui/lint/force-warn/allowed-group-warn-by-default-lint.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // --force-warn $LINT causes $LINT (which is warn-by-default) to warn
// despite $LINT_GROUP (which contains $LINT) being allowed
// compile-flags: --force-warn bare_trait_objects
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


