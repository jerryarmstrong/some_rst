tests/ui/mir/simplify-branch-same.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for SimplifyBranchSame miscompilation.
// run-pass

macro_rules! m {
    ($a:expr, $b:expr, $c:block) => {
        match $a {
            Lto::Fat | Lto::Thin => { $b; (); $c }
            Lto::No => { $b; () }
        }
    }
}

pub enum Lto { No, Thin, Fat }

fn f(mut cookie: u32, lto: Lto) -> u32 {
    let mut _a = false;
    m!(lto, _a = true, {cookie = 0});
    cookie
}

fn main() { assert_eq!(f(42, Lto::Thin), 0) }


