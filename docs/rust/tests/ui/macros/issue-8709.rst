tests/ui/macros/issue-8709.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

macro_rules! sty {
    ($t:ty) => (stringify!($t))
}

macro_rules! spath {
    ($t:path) => (stringify!($t))
}

fn main() {
    assert_eq!(sty!(isize), "isize");
    assert_eq!(spath!(std::option), "std::option");
}


