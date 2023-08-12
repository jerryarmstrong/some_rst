tests/ui/issues/issue-2849.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Foo { Alpha, Beta(isize) }

fn main() {
    match Foo::Alpha {
      Foo::Alpha | Foo::Beta(i) => {}
      //~^ ERROR variable `i` is not bound in all patterns
    }
}


