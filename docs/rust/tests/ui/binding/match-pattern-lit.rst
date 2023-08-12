tests/ui/binding/match-pattern-lit.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


fn altlit(f: isize) -> isize {
    match f {
      10 => { println!("case 10"); return 20; }
      11 => { println!("case 11"); return 22; }
      _  => panic!("the impossible happened")
    }
}

pub fn main() {
    assert_eq!(altlit(10), 20);
    assert_eq!(altlit(11), 22);
}


