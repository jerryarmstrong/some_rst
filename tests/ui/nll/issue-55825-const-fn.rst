tests/ui/nll/issue-55825-const-fn.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #55825
// Tests that we don't emit a spurious warning in NLL mode

// check-pass

const fn no_dyn_trait_ret() -> &'static dyn std::fmt::Debug { &() }

fn main() { }


