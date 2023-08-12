tests/ui/type/issue-67690-type-alias-bound-diagnostic-crash.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #67690
// Rustc endless loop out-of-memory and consequent SIGKILL in generic new type

// check-pass
pub type T<P: Send + Send + Send> = P;
//~^ WARN bounds on generic parameters are not enforced in type aliases

fn main() {}


