tests/ui/issues/issue-9725.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A { foo: isize }

fn main() {
    let A { foo, foo } = A { foo: 3 };
    //~^ ERROR: identifier `foo` is bound more than once in the same pattern
    //~^^ ERROR: field `foo` bound multiple times
}


