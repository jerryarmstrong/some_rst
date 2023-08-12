tests/ui/expr/if/attrs/stmt-expr-gated.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = #[deny(warnings)] if true { //~ ERROR attributes on expressions
    } else if false {
    } else {
    };
}


