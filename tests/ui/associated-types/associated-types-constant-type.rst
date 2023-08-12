tests/ui/associated-types/associated-types-constant-type.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait SignedUnsigned {
    type Opposite;
    fn convert(self) -> Self::Opposite;
}

impl SignedUnsigned for isize {
    type Opposite = usize;

    fn convert(self) -> usize {
        self as usize
    }
}

impl SignedUnsigned for usize {
    type Opposite = isize;

    fn convert(self) -> isize {
        self as isize
    }
}

fn get(x: isize) -> <isize as SignedUnsigned>::Opposite {
    x.convert()
}

fn main() {
    let x = get(22);
    assert_eq!(22, x);
}


