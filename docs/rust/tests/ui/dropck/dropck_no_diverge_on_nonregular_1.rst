tests/ui/dropck/dropck_no_diverge_on_nonregular_1.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue 22443: Reject code using non-regular types that would
// otherwise cause dropck to loop infinitely.

use std::marker::PhantomData;

struct Digit<T> {
    elem: T
}

struct Node<T:'static> { m: PhantomData<&'static T> }


enum FingerTree<T:'static> {
    Single(T),
    // Bug report said Digit after Box would stack overflow (versus
    // Digit before Box; see dropck_no_diverge_on_nonregular_2).
    Deep(
        Box<FingerTree<Node<T>>>,
        Digit<T>,
        )
}

fn main() {
    let ft = //~ ERROR overflow while adding drop-check rules for FingerTree
        FingerTree::Single(1);
}


