tests/ui/expr/if/attrs/builtin-if-attr.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    #[allow(unused_variables)]
    if true {
        let a = 1;
    } else if false {
        let b = 1;
    } else {
        let c = 1;
    }
}


