tests/ui/pattern/pattern-tyvar-2.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Bar { T1((), Option<Vec<isize>>), T2, }

fn foo(t: Bar) -> isize { match t { Bar::T1(_, Some(x)) => { return x * 3; } _ => { panic!(); } } }
//~^ ERROR cannot multiply `Vec<isize>` by `{integer}`

fn main() { }


