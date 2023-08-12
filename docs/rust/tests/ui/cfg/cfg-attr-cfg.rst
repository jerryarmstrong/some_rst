tests/ui/cfg/cfg-attr-cfg.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// main is conditionally compiled, but the conditional compilation
// is conditional too!

// pretty-expanded FIXME #23616

#[cfg_attr(foo, cfg(bar))]
fn main() { }


