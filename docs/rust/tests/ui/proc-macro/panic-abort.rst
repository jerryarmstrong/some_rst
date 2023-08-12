tests/ui/proc-macro/panic-abort.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: building proc macro crate with `panic=abort` may crash the compiler should the proc-macro panic
// compile-flags: --crate-type proc-macro -Cpanic=abort
// force-host
// check-pass


