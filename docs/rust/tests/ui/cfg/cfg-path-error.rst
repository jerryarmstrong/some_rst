tests/ui/cfg/cfg-path-error.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

#[cfg(any(foo, foo::bar))]
//~^ERROR `cfg` predicate key must be an identifier
fn foo1() {}

#[cfg(any(foo::bar, foo))]
//~^ERROR `cfg` predicate key must be an identifier
fn foo2() {}

#[cfg(all(foo, foo::bar))]
//~^ERROR `cfg` predicate key must be an identifier
fn foo3() {}

#[cfg(all(foo::bar, foo))]
//~^ERROR `cfg` predicate key must be an identifier
fn foo4() {}

fn main() {}


