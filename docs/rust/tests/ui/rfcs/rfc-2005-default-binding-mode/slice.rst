tests/ui/rfcs/rfc-2005-default-binding-mode/slice.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn slice_pat() {
    let sl: &[u8] = b"foo";

    match sl {
        [first, remainder @ ..] => {
            let _: &u8 = first;
            assert_eq!(first, &b'f');
            assert_eq!(remainder, b"oo");
        }
        [] => panic!(),
    }
}

fn slice_pat_omission() {
     match &[0, 1, 2] {
        [..] => {}
     };
}

fn main() {
    slice_pat();
    slice_pat_omission();
}


