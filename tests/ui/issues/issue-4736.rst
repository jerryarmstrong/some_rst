tests/ui/issues/issue-4736.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct NonCopyable(());

fn main() {
    let z = NonCopyable{ p: () }; //~ ERROR struct `NonCopyable` has no field named `p`
}


