tests/ui/lint/test-inner-fn.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --test -D unnameable_test_items

#[test]
fn foo() {
    #[test] //~ ERROR cannot test inner items [unnameable_test_items]
    fn bar() {}
    bar();
}

mod x {
    #[test]
    fn foo() {
        #[test] //~ ERROR cannot test inner items [unnameable_test_items]
        fn bar() {}
        bar();
    }
}

fn main() {}


