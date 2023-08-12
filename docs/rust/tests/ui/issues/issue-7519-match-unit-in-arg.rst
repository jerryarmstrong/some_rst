tests/ui/issues/issue-7519-match-unit-in-arg.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

/*
#7519 ICE pattern matching unit in function argument
*/

fn foo(():()) { }

pub fn main() {
    foo(());
}


