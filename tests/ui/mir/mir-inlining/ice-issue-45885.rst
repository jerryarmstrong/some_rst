tests/ui/mir/mir-inlining/ice-issue-45885.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags:-Zmir-opt-level=3

pub enum Enum {
    A,
    B,
}

trait SliceIndex {
    type Output;
    fn get(&self) -> &Self::Output;
}

impl SliceIndex for usize {
    type Output = Enum;
    #[inline(never)]
    fn get(&self) -> &Enum {
        &Enum::A
    }
}

#[inline(always)]
fn index<T: SliceIndex>(t: &T) -> &T::Output {
    t.get()
}

fn main() {
    match *index(&0) { Enum::A => true, _ => false };
}


