tests/ui/pattern/usefulness/match-vec-unreachable.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unreachable_patterns)]

fn main() {
    let x: Vec<(isize, isize)> = Vec::new();
    let x: &[(isize, isize)] = &x;
    match *x {
        [a, (2, 3), _] => (),
        [(1, 2), (2, 3), b] => (), //~ ERROR unreachable pattern
        _ => ()
    }

    let x: Vec<String> = vec!["foo".to_string(),
                              "bar".to_string(),
                              "baz".to_string()];
    let x: &[String] = &x;
    match *x {
        [ref a, _, _, ..] => { println!("{}", a); }
        [_, _, _, _, _] => { } //~ ERROR unreachable pattern
        _ => { }
    }

    let x: Vec<char> = vec!['a', 'b', 'c'];
    let x: &[char] = &x;
    match *x {
        ['a', 'b', 'c', ref _tail @ ..] => {}
        ['a', 'b', 'c'] => {} //~ ERROR unreachable pattern
        _ => {}
    }
}


