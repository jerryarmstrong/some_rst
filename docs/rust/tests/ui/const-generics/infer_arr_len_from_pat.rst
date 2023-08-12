tests/ui/const-generics/infer_arr_len_from_pat.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
//
// see issue #70529

fn as_chunks<const N: usize>() -> [u8; N] {
    loop {}
}

fn main() {
    let [_, _] = as_chunks();
}


