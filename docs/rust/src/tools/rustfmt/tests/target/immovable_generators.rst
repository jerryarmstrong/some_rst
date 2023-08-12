src/tools/rustfmt/tests/target/immovable_generators.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators)]

unsafe fn foo() {
    let mut ga = static || {
        yield 1;
    };
}


