tests/ui/lint/force-warn/lint-group-allow-warnings.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // --force-warn $LINT_GROUP causes $LINT in $LINT_GROUP to warn
// despite all warnings being allowed in module
// warn-by-default lint to warn
// compile-flags: --force-warn nonstandard_style
// check-pass

#![allow(warnings)]

pub fn FUNCTION() {}
//~^ WARN function `FUNCTION` should have a snake case name

fn main() {}


