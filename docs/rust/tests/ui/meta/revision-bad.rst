tests/ui/meta/revision-bad.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Meta test for compiletest: check that when we give the wrong error
// patterns, the test fails.

// run-fail
// revisions: foo bar
// should-fail
// needs-run-enabled
//[foo] error-pattern:bar
//[bar] error-pattern:foo

#[cfg(foo)]
fn die() {
    panic!("foo");
}
#[cfg(bar)]
fn die() {
    panic!("bar");
}

fn main() {
    die();
}


