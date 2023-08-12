tests/ui/rfc-2457/idents-normalized.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct Résumé; // ['LATIN SMALL LETTER E WITH ACUTE']

fn main() {
    let _ = Résumé; // ['LATIN SMALL LETTER E', 'COMBINING ACUTE ACCENT']
}


