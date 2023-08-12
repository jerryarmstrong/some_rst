tests/ui/issues/issue-7344.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]
// pretty-expanded FIXME #23616

#![allow(unreachable_code)]

fn foo() -> bool { false }

fn bar() {
    return;
    !foo();
}

fn baz() {
    return;
    if "" == "" {}
}

pub fn main() {
    bar();
    baz();
}


