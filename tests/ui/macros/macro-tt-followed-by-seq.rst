tests/ui/macros/macro-tt-followed-by-seq.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Regression test for issue #25436: permit token-trees to be followed
// by sequences, enabling more general parsing.

use self::Join::*;

#[derive(Debug)]
#[allow(unused_tuple_struct_fields)]
enum Join<A,B> {
  Keep(A,B),
  Skip(A,B),
}

macro_rules! parse_list {
  ( < $a:expr; > $($b:tt)* ) => { Keep(parse_item!($a),parse_list!($($b)*)) };
  ( $a:tt $($b:tt)* ) => { Skip(parse_item!($a), parse_list!($($b)*)) };
  ( ) => { () };
}

macro_rules! parse_item {
  ( $x:expr ) => { $x }
}

fn main() {
    let list = parse_list!(<1;> 2 <3;> 4);
    assert_eq!("Keep(1, Skip(2, Keep(3, Skip(4, ()))))",
               format!("{:?}", list));
}


