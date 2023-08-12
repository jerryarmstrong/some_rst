tests/ui/suggestions/suggest-remove-refs-3.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    let v = vec![0, 1, 2, 3];

    for (i, _) in & & &
        & &v
        .iter()
        .enumerate() {
        //~^^^^ ERROR `&&&&&Enumerate<std::slice::Iter<'_, {integer}>>` is not an
        println!("{}", i);
    }
}


