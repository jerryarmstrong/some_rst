tests/ui/argument-suggestions/two-mismatch-notes.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Copy, Clone)]
struct Wrapper<T>(T);

fn foo(_: fn(i32), _: Wrapper<i32>) {}

fn f(_: u32) {}

fn main() {
    let w = Wrapper::<isize>(1isize);
    foo(f, w); //~ ERROR arguments to this function are incorrect
}


