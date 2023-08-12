tests/ui/resolve/bad-env-capture3.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: can't capture dynamic environment in a fn item
fn foo(x: isize) {
    fn mth() {
        fn bar() { log(debug, x); }
    }
}

fn main() { foo(2); }


