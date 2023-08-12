tests/ui/pattern/usefulness/slice-patterns-irrefutable.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    let s: &[bool] = &[true; 0];
    let s0: &[bool; 0] = &[];
    let s1: &[bool; 1] = &[false; 1];
    let s2: &[bool; 2] = &[false; 2];

    let [] = s0;
    let [_] = s1;
    let [_, _] = s2;

    let [..] = s;
    let [..] = s0;
    let [..] = s1;
    let [..] = s2;

    let [_, ..] = s1;
    let [.., _] = s1;
    let [_, ..] = s2;
    let [.., _] = s2;

    let [_, _, ..] = s2;
    let [_, .., _] = s2;
    let [.., _, _] = s2;
}


