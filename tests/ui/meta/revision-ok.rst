tests/ui/meta/revision-ok.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Meta test for compiletest: check that when we give the right error
// patterns, the test passes. See all `revision-bad.rs`.

// run-fail
// revisions: foo bar
//[foo] error-pattern:foo
//[bar] error-pattern:bar
// ignore-emscripten no processes

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


