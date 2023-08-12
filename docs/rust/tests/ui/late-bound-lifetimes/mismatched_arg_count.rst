tests/ui/late-bound-lifetimes/mismatched_arg_count.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ensures that we don't ICE when there are too many args supplied to the alias.

trait Trait<'a> {
    type Assoc;
}

type Alias<'a, T> = <T as Trait<'a>>::Assoc;

fn bar<'a, T: Trait<'a>>(_: Alias<'a, 'a, T>) {}
//~^ error: this type alias takes 1 lifetime argument but 2 lifetime arguments were supplied

fn main() {}


