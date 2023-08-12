tests/ui/proc-macro/cfg-eval-fail.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(cfg_eval)]
#![feature(stmt_expr_attributes)]

fn main() {
    let _ = #[cfg_eval] #[cfg(FALSE)] 0;
    //~^ ERROR removing an expression is not supported in this position
}


