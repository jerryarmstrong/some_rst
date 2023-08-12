tests/ui/rfcs/rfc-2005-default-binding-mode/for.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {
    let mut tups = vec![(0u8, 1u8)];

    for (n, m) in &tups {
        let _: &u8 = n;
        let _: &u8 = m;
    }

    for (n, m) in &mut tups {
        *n += 1;
        *m += 2;
    }

    assert_eq!(tups, vec![(1u8, 3u8)]);

    for (n, m) in tups {
        println!("{} {}", m, n);
    }
}


