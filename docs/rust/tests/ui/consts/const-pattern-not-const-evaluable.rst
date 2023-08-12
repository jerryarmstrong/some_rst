tests/ui/consts/const-pattern-not-const-evaluable.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#[derive(PartialEq, Eq)]
enum Cake {
    BlackForest,
    Marmor,
}
use Cake::*;

struct Pair<A, B>(A, B);

const BOO: Pair<Cake, Cake> = Pair(Marmor, BlackForest);
const FOO: Cake = BOO.1;

const fn foo() -> Cake {
    Marmor
}

const WORKS: Cake = Marmor;

const GOO: Cake = foo();

fn main() {
    match BlackForest {
        FOO => println!("hi"),
        GOO => println!("meh"),
        WORKS => println!("möp"),
        _ => println!("bye"),
    }
}


