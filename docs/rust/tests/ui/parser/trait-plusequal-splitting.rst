tests/ui/parser/trait-plusequal-splitting.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Fixes issue where `+` in generics weren't parsed if they were part of a `+=`.

// check-pass

struct Whitespace<T: Clone + = ()> { t: T }
struct TokenSplit<T: Clone +=  ()> { t: T }

fn main() {}


