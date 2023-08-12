tests/ui/higher-rank-trait-bounds/issue-36139-normalize-closure-sig.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Previously the closure's argument would be inferred to
// <S as ITrait<'a>>::Item, causing an error in MIR type
// checking

trait ITrait<'a> {type Item;}

struct S {}

impl<'a> ITrait<'a> for S { type Item = &'a mut usize; }

fn m<T, I, F>(_: F)
    where I: for<'a> ITrait<'a>,
          F: for<'a> FnMut(<I as ITrait<'a>>::Item) { }


fn main() {
    m::<usize,S,_>(|x| { *x += 1; });
}


