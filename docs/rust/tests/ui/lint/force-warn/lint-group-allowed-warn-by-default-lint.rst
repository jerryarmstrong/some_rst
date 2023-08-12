tests/ui/lint/force-warn/lint-group-allowed-warn-by-default-lint.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // --force-warn $LINT_GROUP causes $LINT (which is warn-by-default) to warn
// despite $LINT being allowed in module
// compile-flags: --force-warn rust-2018-idioms
// check-pass

#![allow(bare_trait_objects)]

pub trait SomeTrait {}

pub fn function(_x: Box<SomeTrait>) {}
//~^ WARN trait objects without an explicit `dyn` are deprecated
//~| WARN this is accepted in the current edition
//~| WARN trait objects without an explicit `dyn` are deprecated
//~| WARN this is accepted in the current edition
//~| WARN trait objects without an explicit `dyn` are deprecated
//~| WARN this is accepted in the current edition

fn main() {}


