tests/ui/resolve/typo-suggestion-named-underscore.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const _: () = ();

fn main() {
    a // Shouldn't suggest underscore
    //~^ ERROR: cannot find value `a` in this scope
}

trait Unknown {}

#[allow(unused_imports)]
use Unknown as _;

fn foo<T: A>(x: T) {} // Shouldn't suggest underscore
//~^ ERROR: cannot find trait `A` in this scope


