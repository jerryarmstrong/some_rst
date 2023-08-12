tests/ui/use-import-export.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

mod foo {
    pub fn x() -> isize { return 1; }
}

mod bar {
    pub fn y() -> isize { return 1; }
}

pub fn main() { foo::x(); bar::y(); }


